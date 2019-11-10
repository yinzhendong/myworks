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


def get_person():
    name_list = []
    query = (
        "select name from person_copy"
    )
    cursor.execute(query)
    rows = cursor.fetchall()
    for name in rows:
        name_list.append(name[0])

    return name_list

def update_state(tbname, area):
    """update person, person_all, team set state='Q'"""
    names = get_person()
    for name in names:
        print(name)
        update = (
            "update {} set state='Q' "
            "where name='{}' and area='{}'".format(tbname, name, area)
        )
        print(update)
        execute_sql(update)


def insert_personQualify(tbname, area):
    insert = (
        "insert into {} "
        "(name, sex, id_card, phone, phone_conv, email, dep, area) "
        "select name, sex, id_card, phone, phone_conv, email, dep, area "
        "from person where state='Q' and area='{}'".format(tbname, area)
    )
    print(insert)
    execute_sql(insert)


def make_qualify():
    """
    将各赛区晋级复赛的选手导入到对应的qualify表中
    1. 将赛区晋级的个人赛和编队赛名单分别导入到person_copy表及team_copy表中,
    导入前先判断一下个人赛有没有重名的；编队赛有没有重编队名称的情况
    2. 将person_copy表中的数据插入到person_qualify表及person_all_qualify表中
    3. 将team_copy表中的数据插入到team_qualify表中
    """
    update_state(tbname='person', area='山东分赛区')
    update_state(tbname='person_all', area='山东分赛区')
    insert_personQualify(tbname='person_qualify', area='山东分赛区')
    insert_personQualify(tbname='person_all_qualify', area='山东分赛区')

make_qualify()

