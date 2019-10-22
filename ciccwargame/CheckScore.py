import mysql.connector


from ciccwargame.FindSomeone import sql_assemble


cnx = mysql.connector.connect(
    user = 'root',
    password = '',
    database = 'ciccwargame',
    host = '127.0.0.1',
)

cursor = cnx.cursor()

def get_duplicate_phone():
    """
    查询所有重复的隐藏四位手机号
    :return:
    """
    query = (
        "SELECT DISTINCT(phone),phone_conv FROM person_all "
        "WHERE phone_conv IN "
        "(SELECT phone_conv FROM person_all "
        "GROUP BY phone_conv HAVING COUNT(phone_conv)>1) "
        "ORDER BY phone_conv"
    )

    cursor.execute(query)
    results = cursor.fetchall()
    # 存放重复的手机号
    duplicate_phones = []
    # 临时list用来存放重复的手机号
    temp_list = []
    for result in results:
        if result[0] not in temp_list:
            temp_list.append(result[0])
        else:
            duplicate_phones.append(result[1])
    # print(str(len(duplicate_phones)) + " duplicate phone in all person!")
    # print(duplicate_phones)
    return duplicate_phones


def check_duplicate():
    """
    检查成绩表中是否有已知的手机号重复人员
    """
    for duplicate_phone in get_duplicate_phone():
        query = (
        "SELECT * FROM score WHERE phone='{}'".format(duplicate_phone)
    )
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            print("Duplicate phone in score:")
            print('---------------------')
            print(results)
            print("Local DB found:")
            print('---------------------')
            rows = sql_assemble(name='', phone=duplicate_phone)
            for row in rows:
                if row:
                    print(row)
    print("No duplicate phone in score.")
    print('---------------------')


def check_score():
    """
    检查是否存在有成绩但是在人员信息中没有记录的情况
    """
    query = (
        "SELECT s.name, s.phone, s.area, s.first_score, s.second_score, "
        "s.third_score, s.forth_score, s.fifth_score "
        "FROM score s LEFT JOIN person_all p ON s.phone = p.phone "
        "AND LEFT(s.area,2)=LEFT(p.area,2) WHERE p.name is NULL "
        "ORDER BY p.id"
    )
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        # print(results)
        # print("No duplicate phone in score.")
        print(str(len(results)) + " Person have score are NOT in all person!")
        print('---------------------')
        for result in results:
            print(result)


check_duplicate()
check_score()


cursor.close()
cnx.close()