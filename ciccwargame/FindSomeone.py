import mysql.connector


def find_someone(sql):
    cnx = mysql.connector.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            password = '',
            database = 'ciccwargame',
    )
    cursor = cnx.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


def sql_assemble(name, phone):
    sqllist = []
    sqllist.append("SELECT name, phone, area FROM person "
                   "WHERE phone='{}' OR name='{}'".format(phone, name))
    sqllist.append("SELECT name, phone, area FROM person_all "
                   "WHERE phone='{}' OR name='{}'".format(phone, name))
    sqllist.append("SELECT leader_name, leader_phone, member_name, "
                   "member_phone, area FROM team WHERE leader_phone='{}' "
                   "OR member_phone='{}'".format(phone, phone))
    sqllist.append("SELECT leader_name, leader_phone, member_name, "
                   "member_phone FROM team WHERE leader_name='{}' "
                   "OR member_name='{}'".format(name, name))
    sqllist.append("SELECT name, phone, area FROM person "
                   "WHERE phone_conv='{}' OR name='{}'".format(phone, name))
    sqllist.append("SELECT name, phone, area FROM person_all "
                   "WHERE phone_conv='{}' OR name='{}'".format(phone, name))
    sqllist.append("SELECT leader_name, leader_phone, member_name, "
                   "member_phone, area FROM team WHERE leader_phone_conv='{}' "
                   "OR member_phone_conv='{}'".format(phone, phone))
    sqllist.append("SELECT leader_name, leader_phone, member_name, "
                   "member_phone, area FROM team WHERE leader_name='{}' OR "
                   "member_name='{}'".format(name, name))
    result = []
    for sql in sqllist:
        # print(sql)
        result.append(find_someone(sql))
    return result


rows = sql_assemble(name='', phone='13623616833')
for row in rows:
    if row:
        print(row)
