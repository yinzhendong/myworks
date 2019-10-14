import os
import math
import subprocess


from mrms.utils.file_info import get_file_info


base_dir = (
    '/home/trent/data/workspace/PycharmProjects/python_works/mrms/resources/'
)
file = os.path.join(base_dir, 'video/1.flv')
# file = '/home/trent/data/workspace/PycharmProjects/python_works/mrms/' \
#        'resources/video/1.mkv'


def split_video(file):
    # 调用函数获取文件基本信息
    file_info = get_file_info(file)

    # 获取文件后缀名
    # file_suffix = os.path.splitext(file)[1].replace('.', '')
    file_suffix = os.path.splitext(file)[1]
    # print(file_suffix)

    # 计算文件时长
    file_duration = math.ceil(file_info['duration'] / 1000 / 60)
    # print(file_duration)

    for x in range(file_duration):
        split_command = (
                'ffmpeg -ss ' + str(x * 60) +
                ' -t 60 -i '  + file +
                ' -acodec copy -vcodec copy ' + '-y ' +
                file + '-' + str(x) + file_suffix
        )
        print(split_command)
        subprocess.run(split_command, shell=True)

split_video(file)
