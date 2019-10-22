import mysql.connector


def copy_person(name):
    cnx = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='',
        database='ciccwargame',
    )
    cursor = cnx.cursor()

    insert_from_person_all_to_person_sql = (
        "INSERT INTO person (name, sex, id_card, phone, phone_conv, email, "
        "dep, area, first_score, second_score, third_score, forth_score, "
        "fifth_score, max_score, total_score, average_score) "
        "SELECT name, sex, id_card, phone, phone_conv, email, dep, area, "
        "first_score, second_score, third_score, forth_score, fifth_score, "
        "max_score, total_score, average_score "
        "FROM person_all WHERE name='{}'".format(name)
    )
    cursor.execute(insert_from_person_all_to_person_sql)
    cnx.commit()
    cursor.close()
    cnx.close()

def copy_team(team_name):
    cnx = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='',
        database='ciccwargame',
    )
    cursor = cnx.cursor()

    insert_from_team_to_team_sql = (
        "INSERT INTO team (teamname, sex, id_card, phone, phone_conv, email, "
        "dep, area, first_score, second_score, third_score, forth_score, "
        "fifth_score, max_score, total_score, average_score) "
        "SELECT name, sex, id_card, phone, phone_conv, email, dep, area, "
        "first_score, second_score, third_score, forth_score, fifth_score, "
        "max_score, total_score, average_score "
        "FROM person_all WHERE name='{}'".format(name)
    )
    cursor.execute(insert_from_person_all_to_person_sql)
    cnx.commit()
    cursor.close()
    cnx.close()

# copy_person('')
# copy_person('')
