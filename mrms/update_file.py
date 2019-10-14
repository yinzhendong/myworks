import mysql.connector


from mrms.utils.read_config import get_db_con

conf = get_db_con()
print(conf)

cnx = mysql.connector.connect(conf)

cursor = cnx.cursor()
query = (
    "select * from program"
)

cursor.execute(query)
results = cursor.fecthall()

print(results)
