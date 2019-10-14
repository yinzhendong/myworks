import mysql.connector


config = {
    'host': '127.0.0.1',
    'port': '3306',
    'user': 'root',
    'password': 'root',
    'database': 'mrms',
}
cnx = mysql.connector.connect(**config)


def sql_query(**kw):
    """Query MySQL

    """
    query = (
        "select {} from {}".format(kw['column'], kw['tbname'])
    )
    cursor = cnx.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    cursor.close()
    cnx.close()

context = {
    'tbname': 'program',
    'column': '*',
}
sql_query(**context)


