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


def make_person_qualify(phone, area):
    sql = (
        "update person_final set state='qualified' "
        "where phone='{}' and area='{}'".format(phone, area)
    )
    print(sql)
    # execute_sql(sql)


def make_team_qualify(leaderphone, memberphone, area):
    sql = (
        "update team_final set state='qualified' "
        "where leader_phone='{}' and member_phone='{}' and area='{}'".format(
            leaderphone, memberphone, area)
        )
    print(sql)
    # execute_sql(sql)


def get_namelist(file):
    # 从文本文件里读取姓名、赛区、编队名称信息，用list返回
    namelist = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            namelist.append(line.strip('\n'))
    return namelist


def handle_person():
    namelist = get_namelist('person.txt')
    for name in namelist:
        names = name.split('\t')
        area = names[1]
        phone = names[3]
        make_person_qualify(phone, area)


def handl_team():
    teamlist = get_namelist('team.txt')
    for team in teamlist:
        print(team)
        names = team.split('\t')
        print(names)
        leaderphone = names[4]
        memberphone = names[7]
        area = names[1]
        print('leaderphone={} memberphone={} area={}'.format(
            leaderphone, memberphone, area))
        make_team_qualify(leaderphone, memberphone, area)


def main():
    handle_person()
    # handl_team()

main()