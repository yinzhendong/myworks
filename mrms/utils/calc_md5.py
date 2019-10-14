import hashlib
import os
import datetime


# base_dir = '/home/trent/data/workspace/PycharmProjects/python_works/mrms/'

# file_path = os.path.join(
#     base_dir,
#     'resources/doc/1.txt'
#     'resources/video/Hidden.Desire.1991.BD1080P.X264.AAC.CHS.Mp4Ba.mp4'
# )


def calc_md5(file):
    if not os.path.isfile(file):
        return 'file not exist!'
    md5_value = hashlib.md5()

    with open(file, 'rb') as f:
        while True:
            data_flow = f.read(8192)
            if not data_flow:
                break
            md5_value.update(data_flow)
    f.close()
    return md5_value.hexdigest()

# 测试MD5计算时间
# start_time = datetime.datetime.now()
# print(calc_md5(file_path).upper())
# end_time = datetime.datetime.now()
# print('calc time is: {}'.format((end_time - start_time).seconds))
# print(os.path.getsize(file_path))
