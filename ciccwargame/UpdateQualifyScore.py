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


def update_person_score(tb_name):
    """
    更新score中的成绩到person_qualify
    """
    sql = (
        "UPDATE person_qualify as p INNER JOIN score as s "
        "ON p.phone = s.phone AND LEFT(s.area,2)=LEFT(p.area,2)"
        "SET p.first_score = s.first_score, "
        "p.second_score = s.second_score, "
        "p.third_score = s.third_score, "
        "p.forth_score = s.forth_score, "
        "p.fifth_score = s.fifth_score, "
        "p.max_score = s.max_score, "
        "p.total_score = s.total_score, "
        "p.average_score = s.average_score"
    ).replace('person_qualify', tb_name)
    execute_sql(sql)


def update_team_score(column):
    sql = (
        "UPDATE team_qualify t LEFT JOIN person_all_qualify p "
        "ON t.leader_name=p.name "
        "AND t.leader_phone=p.phone "
        "AND t.leader_id=p.id_card "
        "AND LEFT(t.area,2)=LEFT(p.area,2)"
        "SET t.leader_max_score=p.max_score "
        "WHERE p.max_score IS NOT NULL"
    ).replace('leader', column)
    execute_sql(sql)


# update score
update_person_score('person_qualify')
update_person_score('person_all_qualify')
update_team_score('leader')
update_team_score('member')

cursor.close()
cnx.close()
