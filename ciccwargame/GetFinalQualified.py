import mysql.connector


cnx = mysql.connector.connect(
    user = 'root',
    password = '',
    host = '127.0.0.1',
    database = 'ciccwargame',
)
cursor = cnx.cursor()


def execute_sql(sql):
    """
    Execute sql string
    """
    try:
        cursor.execute(sql)
    except Exception as e:
        cnx.rollback()
        print(sql + "--> Failed!")
    else:
        cnx.commit()
        # print(sql + "--> Success!")


def get_final_person():
    sql = (
        "select area, phone, name, max_score from person_final "
        "where state='' or state is null "
        "order by max_score desc "
    )
    cursor.execute(sql)
    rows = cursor.fetchall()
    # print(rows)
    return rows


def get_final_team():
    sql = (
        "select area, leader_phone, team_name, "
        "IFNULL(leader_max_score,0)+IFNULL(member_max_score,0) AS max_score "
        "from team_final "
        "where state='' or state is null "
        "order by max_score desc "
    )
    cursor.execute(sql)
    rows = cursor.fetchall()
    # print(rows)
    return rows


def mark_qualified(records, quota, type):
    sql = []
    for record in records:
        area = record[0]
        phone = record[1]
        name = record[2]
        if quota[area] < 6 and sum(quota.values()) < 22:
            # print(quota[area], sum(quota.values()))
            quota[area] += 1
            print(area, name, phone)
            if type == 'person':
                sql.append(
                    "update person_final set state='qualified' "
                    "where name='{}' and phone='{}' and area='{}'".format(
                        name, phone, area))
            else:
                sql.append(
                    "update team_final set state='qualified' "
                    "where team_name='{}' and leader_phone='{}' "
                    "and area='{}'".format(name, phone, area))

    for k, v in quota.items():
        print('{} has {} quotas'.format(k, v))
    print(sum(quota.values()))
    # print(sql)
    return sql


quota = {
    '安徽分赛区': 0, '北京分赛区': 0, '江苏分赛区': 0, '重庆分赛区': 0, '浙江分赛区': 0,
    '山西分赛区': 0, '陕西分赛区': 0, '山东分赛区': 0, '广西分赛区': 0, '湖南分赛区': 0,
    '湖北分赛区': 0, '吉林分赛区': 0, '河南分赛区': 0,
}


def main():
    # update_persons = mark_qualified(get_final_person(), quota, type='person')
    # for update_person in update_persons:
    #     print(update_person)
    #     execute_sql(update_person)


    update_teams = mark_qualified(get_final_team(), quota, type='team')
    for update_team in update_teams:
        print(update_team)
        execute_sql(update_team)

main()

cursor.close()
cnx.close()
