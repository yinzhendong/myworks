import os, logging, mysql.connector



from works.calc_md5 import calc_md5


def find_duplicate_files(path):
    """Find the duplicate files in given path."""

    # log into file 'DeleteDirs.log'
    logging.basicConfig(filename='DuplicateFiles.log',
                        format='%(asctime)s %(levelname)s:%(message)s',
                        level=logging.DEBUG, datefmt='%Y-%m-%d %I:%M:%S')
    logging.info("Find the duplicate file in --> '{}'.".format(path))

    # Check path is exists.
    if not os.path.exists(path):
        print('Path --> {} --> not exists.'.format(path))
        logging.info('Path --> {} --> not exists.'.format(path))

    duplicate_files = []
    # Get all files in path and calculate the MD5.
    for root, dirs, files in os.walk(path):
        for file in files:
            abs_file = os.path.join(root, file)
            hash = calc_md5(abs_file)
            print("{} hash --> {}".format(abs_file, hash))
            dic = {'name': abs_file, 'hash': hash}
            insert_file_to_db(abs_file, hash)
            duplicate_files.append(dic)
    return duplicate_files

def insert_file_to_db(name, hash):
    cnx = mysql.connector.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        database='mrms',
    )
    sql = (
        "insert into files (path, hash) values ('{}','{}')".format(name, hash)
    )
    cursor = cnx.cursor()
    print(sql)
    cursor.execute(sql)
    cnx.commit()
    cursor.close()
    cnx.close()

path = '/home/trent/data/tmp/'
files = find_duplicate_files(path)



# all_hash = []
# for file in files:
#     all_hash.append(file['hash'])
#
# for hash in all_hash:
#     if all_hash.count(hash) > 1:
#         print(hash)
#         for file in files:
#             if file['hash'] == hash:
#                 print(file['name'])
#