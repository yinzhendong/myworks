import mysql.connector

cnx_cicc = mysql.connector.connect(user = 'root',
                              password = '',
                              host = '127.0.0.1',
                              port = '3306',
                              database = 'ciccwargame')

cnx_enroll = mysql.connector.connect(user = 'root',
                                   password = '',
                                   host = '127.0.0.1',
                                   port = '3306',
                                   database = 'enroll')
def get_and_insert_score():
    cursor_cicc = cnx_cicc.cursor(buffered=True)
    cursor_enroll = cnx_enroll.cursor(buffered=True)

    sql_get_scores = (
        "SELECT name, phone, first_score, second_score, third_score, "
        "forth_score, fifth_score, max_score, total_score, average_score, area "
        "FROM score"
    )

    cursor_cicc.execute(sql_get_scores)
    rows = cursor_cicc.fetchall()
    for row in rows:
        name = row[0]
        phone = row[1]
        first_score = row[2]
        second_score = row[3]
        third_score = row[4]
        forth_score = row[5]
        fifth_score = row[6]
        max_score = row[7]
        total_score = row[8]
        average_score = row[9]
        area = row[10]

        sql_insert_scores = (
            "INSERT INTO score (name, phone, first_score, second_score, "
            "third_score, forth_score, fifth_score, max_score, total_score, "
            "average_score, area) VALUES('{}', '{}', {}, {}, {}, {}, {}, {}, "
            "{}, {}, '{}')".format(
                name, phone, first_score, second_score, third_score,
                forth_score, fifth_score, max_score, total_score,
                average_score, area
            ).replace('None', 'NULL')
        )
        cursor_enroll.execute(sql_insert_scores)

    cursor_cicc.close()
    cursor_enroll.close()
    cnx_enroll.commit()

    cnx_cicc.close()
    cnx_enroll.close()

def insert_score(sql):
    pass


get_and_insert_score()
