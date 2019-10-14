import mysql.connector
import shutil
import os
# windows version

# where to copy
dst = 'c:\\tmp\\'

cnx = mysql.connector.connect(
    user = 'root',
    password = '',
    host = '127.0.0.1',
    database = 'chdrms',
)

cursor = cnx.cursor()

query = (
    "SELECT program.name, serial.name, serial.file_path "
    "FROM serial LEFT JOIN program ON serial.program_id=program.id "
    "WHERE file_path NOT LIKE '/data2/upload%' ORDER BY file_path"
)

cursor.execute(query)
results = cursor.fetchall()

for row in results:
    program_name = row[0].replace('&nbsp;',' ').replace('&#160;', ' ').rstrip()
    serial_name = row[1].replace('&nbsp;',' ').replace('&#160;', ' ').rstrip()
    file_path = row[2]
    # print(program_name, " + ", serial_name, " + ", file_path)

    # make directory by program_name
    if not os.path.exists(dst+program_name):
        os.makedirs(dst+program_name)

    # assemble directory
    dir = dst+program_name
    file = 'c:\\chdbmc.sql'

    # copy file to dst change hash name to file actual name
    # shutil.copy(file, dir+'\\'+serial_name+os.path.splitext(file)[1])
    try:
        shutil.copy(file, dir+'\\'+serial_name)
        # shutil.copy(file_path, dir+'\\'+serial_name)
        print('copyed ' + file_path + ' to ' + dst + ' OK.')
    except FileNotFoundError:
        print(file_path + " NOT exist.")
        with open('file_not_exist.txt', 'a') as f_obj:
            f_obj.write(file_path + '\n')

cnx.close()
print('All file copyed success!')
