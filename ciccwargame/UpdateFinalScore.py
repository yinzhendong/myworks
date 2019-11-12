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


def update_phone(tb_name, dst_column, src_column):
    """
    set the table's phone_conv=phone
    ex: update person set phone_conv=phone
    then set table's phone_conv middle 4 replace with *
    ex: 13912345678 to 139****5678
    """
    sql_copy = (
        "update {} set {}={}".format(tb_name, dst_column, src_column)
    )

    sql_update = (
        "UPDATE {} SET {}=REPLACE({},SUBSTR({},4,4),'****')".format(
            tb_name, dst_column, dst_column, dst_column)
    )

    for sql in (sql_copy, sql_update):
        execute_sql(sql)


def insert_person(column):
    """
    将编队报名team表中不在person_all表中的信息插入person_all表中
    """
    sql = (
        "INSERT INTO person_all_final"
        "(name,sex,id_card,phone,phone_conv,email,dep,area) "
        "SELECT leader_name,leader_sex,leader_id,leader_phone,"
        "leader_phone_conv, leader_email,leader_dep,t.area "
        "FROM team_final t LEFT JOIN person_all_final pa "
        "ON t.leader_name=pa.name "
        # "AND t.leader_id=pa.id_card "
        "AND t.leader_phone=pa.phone "
        "WHERE pa.name IS NULL "
        "ORDER BY t.leader_name".replace('leader', column)
    )
    execute_sql(sql)


def update_person_score(tb_name):
    """
    更新score中的成绩到person
    """
    sql = (
        "UPDATE person_final as p INNER JOIN score as s "
        "ON p.phone = s.phone "
        "SET p.first_score = s.first_score, "
        "p.second_score = s.second_score, "
        "p.third_score = s.third_score, "
        "p.forth_score = s.forth_score, "
        "p.fifth_score = s.fifth_score, "
        "p.max_score = s.max_score, "
        "p.total_score = s.total_score, "
        "p.average_score = s.average_score"
    ).replace('person_final', tb_name)
    execute_sql(sql)


def update_team_score(column):
    sql = (
        "UPDATE team_final t LEFT JOIN person_all_final p "
        "ON t.leader_name=p.name "
        "AND t.leader_phone=p.phone "
        # "AND t.leader_id=p.id_card "
        "AND LEFT(t.area,2)=LEFT(p.area,2)"
        "SET t.leader_max_score=p.max_score "
        "WHERE p.max_score IS NOT NULL"
    ).replace('leader', column)
    execute_sql(sql)


def main():
    # update phone
    update_phone('person_final', 'phone_conv', 'phone')
    update_phone('person_all_final', 'phone_conv', 'phone')
    update_phone('team_final', 'leader_phone_conv', 'leader_phone')
    update_phone('team_final', 'member_phone_conv', 'member_phone')

    # insert team person to person_all
    insert_person('leader')
    insert_person('member')

    # update score
    update_person_score('person_final')
    update_person_score('person_all_final')
    update_team_score('leader')
    update_team_score('member')

main()

cursor.close()
cnx.close()
