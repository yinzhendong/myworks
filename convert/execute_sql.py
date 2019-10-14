import mysql.connector


def execute_sql(sql, type='others'):
    """Execute sql string
    Example:
    query = ("select * from program")
    update = ("update program set pname='myPromgram'")
    insert = (
    "insert into program (id, pname, serial_num) values('3', 'yourProgram', '5')"
    )
    delete = ("delete from program where id=3")
    execute_sql(update)
    execute_sql(insert)
    execute_sql(delete)
    rows = execute_sql(query, 'query')
    """
    config = {
        'host': '127.0.0.1',
        'port': '3306',
        'user': 'root',
        'password': 'root',
        'database': 'chdbmc',
    }
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    if type == 'query':
        try:
            cursor.execute(sql)
        except Exception as err:
            cnx.rollback()
            print(sql + '--> Failed!')
        else:
            return  cursor.fetchall()
    else:
        try:
            cursor.execute(sql)
        except Exception as err:
            cnx.rollback()
        else:
            cnx.commit()

    cursor.close()
    cnx.close()
