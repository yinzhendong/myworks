import mysql.connector


cnx = mysql.connector.connect(
    user = 'root',
    password = '',
    host = '127.0.0.1',
    database = 'ciccwargame',
)

cursor = cnx.cursor()


def get_score_all_anhui():
    """从score表中查询所有安徽赛区人员的手机号"""
    query = (
        "select phone from score where area like '安徽%'"
    )
    cursor.execute(query)
    results = cursor.fetchall()
    return results


def convert_score_anhui2jiangsu():
    # 用所有score表中安徽赛区的人员手机号去person_all表中查询是江苏赛区的人员
    persons = get_score_all_anhui()
    for person in persons:
        query = (
            "select phone, area from person_all "
            "where phone='{}' and area='江苏分赛区'".format(person[0])
        )
        # print(query)
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            if row:
                print(row)
                # 更新score表中显示安徽赛区，其实是江苏赛区的人员
                update = (
                    "update score set area='江苏赛区' "
                    "where phone='{}' and area='安徽赛区'".format(row[0])
                )
                print(update)
                cursor.execute(update)
                cnx.commit()

convert_score_anhui2jiangsu()

cursor.close()
cnx.close()
