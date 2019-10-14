import os
import configparser

from mrms.execute_sql import execute_sql
from mrms.utils.convert_queue import convert_queue
from mrms.utils.read_config import get_base_dir

# 调用read_path.py读取配置文件取得base_dir组装文件路径
# base_dir = get_base_dir()
# file = os.path.join(base_dir, 'resources/video/1.avi')
# print(file)


convert_waiting_queue = []

def convert_video():
    get_waiting_convert_queue = (
        "select path from files where convert_status=2 limit 5"
    )
    records = execute_sql(get_waiting_convert_queue, 'query')
    for record in records:
        convert_waiting_queue.append(record[0])
    return convert_waiting_queue

# print(convert_video())
convert_queue(convert_video())
