import mysql.connector


cnx = mysql.connector.connect(
    user = 'root',
    password = '',
    host = '127.0.0.1',
    database = 'enroll',
)

cursor = cnx.cursor()

def insert_single_to_forimported():
    query = (
        "INSERT INTO forimported(team_name, name, phone, dep, mail) "
        "SELECT 'singl', name, phone, dep, email FROM person"
    )
    print(query)
    cursor.execute(query)

insert_single_to_forimported()

def set_sigle_num():
    select_name = (
        "SELECT DISTINCT(name) FROM forimported ORDER BY name"
    )
    cursor.execute(select_name)
    names = cursor.fetchall()
    # print(names)
    changed_names = (
        [names[2*i:2*(i+1)] for i in range(int((len(names)+1)/2))]
    )

    num = 5000
    for changed_name in changed_names:
        for name in changed_name:
            name = name[0]
            set_num_query = (
                "UPDATE forimported SET num={} "
                "WHERE name='{}'".format(num, name)
            )
            # print(num)
            cursor.execute(set_num_query)
            print(set_num_query)
        num = num + 1

set_sigle_num()

cursor.close()
cnx.close()