import os.path

from mrms.utils.calc_md5 import calc_md5
from mrms.execute_sql import execute_sql


def get_all_files(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(
                {
                    'name': file,
                    'path': os.path.join(root, file)
                }
            )
    return file_list

path = '/home/trent/data/workspace/PycharmProjects/python_works/mrms/resources/'
rows = get_all_files(path)
for row in rows:
    name = row['name'].rsplit('.', 1)[0]
    suffix = row['name'].rsplit('.', 1)[1]
    path = row['path']
    hash = calc_md5(row['path'])
    size = os.path.getsize(row['path'])
    sql_insert = (
        "INSERT INTO files (name, path, hash, size, suffix) "
        "VALUES ('{}', '{}', '{}', '{}', '{}')"
            .format(name, path, hash, size, suffix)
    )
    print(sql_insert)
    print(name)
    print(suffix)
    print(hash)
    print(size)
    execute_sql(sql_insert)

