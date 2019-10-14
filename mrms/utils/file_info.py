# 用pymediainfo模块获取文件信息，不要用Linux下的mediainfo去调用获取
# 使用现成的封装更好
# 作者：Trent
# 创建日期：2019年9月12日
import os


from pymediainfo import MediaInfo
# from mrms.utils.get_all_file import get_all_file
from mrms.utils.calc_md5 import calc_md5


# base_dir = '/home/trent/data/workspace/PycharmProjects/python_works/mrms/'
# file = os.path.join(base_dir, 'resources/video/1.avi')
# path = os.path.join(base_dir, 'resources/')


def get_file_info(file):
    file_info = {}
    mi = MediaInfo.parse(file)

    for track in mi.tracks:
        # get file format
        if track.track_type == 'General':
            file_info.update({'format': track.format})

        # get file video info
        if track.track_type == 'Video':
            file_info.update(
                {
                    'duration': track.duration,
                    'width': track.width,
                    'height': track.height,
                    'vb': track.bit_rate,
                }
            )

        # get file audio info
        if track.track_type == 'Audio':
            file_info.update({'ab': track.bit_rate})
    file_info.update({'size': os.path.getsize(file)})
    file_info.update({'name': os.path.basename(file)})
    file_info.update({'hash': calc_md5(file)})
    print(file_info)
    return file_info

# get_file_info(
#     '/home/trent/data/workspace/PycharmProjects/python_works/mrms/resources/'
#     'video/1.avi'
# )
# print(get_file_info(file))

# 扫描整个目录获取文件信息，调试用
# file_path = get_all_file(path)[0]
# for path in file_path:
#     get_video_info(path)
#     print(get_video_info(path))
#
# file_name = get_all_file(path)[1]
# for name in file_name:
#     print(name)
