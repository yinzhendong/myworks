import mysql.connector


def get_team_info():
    cnx = mysql.connector.connect(
        user='root',
        password='',
        host='127.0.0.1',
        port='3306',
        database='moziai',
    )
    cursor = cnx.cursor()
    sql = (
        "SELECT * FROM team WHERE `status`=2"
    )
    cursor.execute(sql)
    rows = cursor.fetchall()

    cursor.close()
    cnx.close()

    return rows


def show_team_info():
    teams = get_team_info()
    for team in teams:
        team_name = team[1]
        print(team_name)


show_team_info()
