import mysql.connector


def connect_to_mysql():
    config = {
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'port': '3306',
        'database': 'mrms',
    }

    cnx = mysql.connector.connect(**config)
    cnx.close()

connect_to_mysql()