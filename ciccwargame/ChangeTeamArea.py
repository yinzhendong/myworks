import mysql.connector


def change_team_area():
    cnx = mysql.connector.connect(
        user = 'root',
        password = '',
        database = 'ciccwargame',
        host = '127.0.0.1'
    )

    cursor_query = cnx.cursor(buffered=True)
    cursor_update = cnx.cursor(buffered=True)

    query = (
        "select team_name, area from t_jiangsu"
    )

    cursor_query.execute(query)
    results = cursor_query.fetchall()
    for row in results:
        team_name = row[0]
        area = row[1]
        cursor_update.execute(make_team_update_sql(team_name, area))
        cnx.commit()
        # print(make_team_update_sql(team_name, area))
    cursor_query.close()
    cursor_update.close()
    cnx.close()

def make_team_update_sql(team_name, area):
    update = (
        "update team set area='江苏分赛区' "
        "where team_name='{}' and area='{}'".format(team_name, area)
    )
    return update


change_team_area()
