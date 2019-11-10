import mysql.connector


cnx = mysql.connector.connect(
    user = 'root',
    password = '',
    host = '127.0.0.1',
    database = 'enroll',
)

cursor = cnx.cursor()

def insert_team_to_forimported(column):
    query = (
        "INSERT INTO forimported(team_name, name, phone, dep, mail) "
        "SELECT team_name,leader_name, leader_phone, leader_dep, "
        "member_email FROM team".replace('leader', column)
    )
    print(query)
    cursor.execute(query)

insert_team_to_forimported('leader')
insert_team_to_forimported('member')

def set_team_num():
    select_team_name = (
        "SELECT DISTINCT(team_name) FROM forimported ORDER BY team_name"
    )
    cursor.execute(select_team_name)
    team_names = cursor.fetchall()

    num = 1001
    for team_name in team_names:
        team_name = team_name[0]
        set_num_query = (
            "UPDATE forimported SET num={} "
            "WHERE team_name='{}'".format(num, team_name)
        )
        cursor.execute(set_num_query)
        # print(set_num_query)
        num = num + 1

set_team_num()

cursor.close()
cnx.close()