import mysql.connector


def get_phone_sql(name, area):
    cnx = mysql.connector.connect(
        user='root',
        password='',
        host='127.0.0.1',
        database='ciccwargame',
    )
    cursor = cnx.cursor()
    sql = (
        "select phone from person_all_final where name='{}' and area='{}'".format(
            name, area
        )
    )
    # print(sql)
    cursor.execute(sql)
    phone = cursor.fetchall()

    cursor.close()
    cnx.close()

    return phone


def get_namelist(file):
    namelist = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            namelist.append(line.strip('\n'))
    return namelist


def get_phone():
    namelist = get_namelist('people.txt')
    for name in namelist:
        phone = get_phone_sql(name, area='北京分赛区')
        if phone:
            print(name, phone[0][0])


def main():
    get_phone()

main()