import mysql.connector


def change_person_area():
    cnx = mysql.connector.connect(
        user = 'root',
        password = '',
        database = 'ciccwargame',
        host = '127.0.0.1'
    )

    cursor_query = cnx.cursor(buffered=True)
    cursor_update = cnx.cursor(buffered=True)

    query = (
        "select name, phone, area from sheet1"
    )

    cursor_query.execute(query)
    results = cursor_query.fetchall()
    for row in results:
        name = row[0]
        phone_conv = row[1]
        area = row[2]
        cursor_update.execute(
            make_person_update_sql('person', name, phone_conv, area))
        cursor_update.execute(
            make_person_update_sql('person_all', name, phone_conv, area))
        cnx.commit()
    cursor_query.close()
    cursor_update.close()
    cnx.close()

def make_person_update_sql(table, name, phone_conv, area):
    update = (
        "update {} set area='江苏分赛区' where name='{}' and phone_conv='{}' "
        "and area='{}'".format(table, name, phone_conv, area)
    )
    return update


change_person_area()
