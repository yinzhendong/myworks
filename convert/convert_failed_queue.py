# import sys
# import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)


from convert.convert_queue import convert_queue
from convert.execute_sql import execute_sql


# Assemble covert failed file list, [('original file path', 'target file path')]
# Example:
# convert_waiting_queue = [
# ('/home/trent/store/store/5DB85304DE4FEC2D0FC7ABD381A092B5.mkv',
# '/home/trent/store/media/video/5DB85304DE4FEC2D0FC7ABD381A092B5/1920_800.mp4')
# ]
convert_waiting_queue = []

def get_failed_file_list():
    sql_get_failed = (
        "SELECT  b.file_path, t.file_path, b.file_hash, b.id "
        "FROM boful_file b LEFT JOIN transcode_file t ON b.id=t.boful_file_id "
        "WHERE b.transcode_state=3"
    )
    records = execute_sql(sql_get_failed, type='query')
    for row in records:
        src_path = row[0]
        dst_path = row[1]
        file_hash = row[2]
        id = row[3]
        file = [src_path, dst_path, file_hash, id]
        convert_waiting_queue.append(file)
    return convert_waiting_queue


def update_state(file_hash, boful_file_id):
    sql_update_boful_file_status = (
        "update boful_file set transcode_state=2 "
        "where file_hash='{}'".format(file_hash)
    )
    sql_update_transcode_file_status = (
        "update transcode_file set transcode_state=2 "
        "where boful_file_id='{}'".format(boful_file_id)
    )
    # print(sql_update_boful_file_status)
    # print(sql_update_transcode_file_status)
    execute_sql(sql_update_boful_file_status)
    execute_sql(sql_update_transcode_file_status)

# 将转码失败文件发送到转码队列进行转码
convert_queue(get_failed_file_list())

# 更新boful_file和tanscode_file转码状态为2（转码成功）
# get_failed_file_list()
# print(convert_waiting_queue)
for file in convert_waiting_queue:
    file_hash = file[2]
    boful_file_id = file[3]
    update_state(file_hash, boful_file_id)
