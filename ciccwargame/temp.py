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


def insert_person(tbname, name, area):
    sql = (
        "insert into {} (name, phone, email, dep, area) "
        "select name, phone, email, dep, area from person "
        "where name='{}' and area='{}'".format(tbname, name, area)
    )
    print(sql)
    # execute_sql(sql)


def insert_team(leadername, membername, area):
    sql = (
        "insert into team_final "
        "(team_name, leader_name, leader_phone, leader_dep, "
        "member_name, member_phone, member_dep, area) "
        "select team_name, leader_name, leader_phone, leader_dep, "
        "member_name, member_phone, member_dep, area from team "
        "where leader_name='{}' and member_name='{}' and area='{}'".format(
            leadername, membername, area
        )
    )
    print(sql)


def make_namelist(file):
    # 从文本文件里读取姓名，用list返回
    namelist = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            namelist.append(line.strip('\n'))
    return namelist


def handle_person():
    namelist = make_namelist('person.txt')
    for name in namelist:
        insert_person('person', name, '山西分赛区')
        insert_person('person_all', name, '山西分赛区')


def handl_team():
    teamlist = make_namelist('team.txt')
    print(teamlist)
    for team in teamlist:
        names = team.split(' ')
        leadername = names[0]
        membername = names[1]
        # print('leadername={} membername={}'.format(leadername, membername))
        insert_team(leadername, membername, '山西分赛区')


def main():
    # handle_person()
    handl_team()

main()