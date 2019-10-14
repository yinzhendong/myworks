# 用pymediainfo模块获取文件信息，不要用Linux下的mediainfo去调用获取
# 使用现成的封装更好
# 作者：Trent
# 创建日期：2019年9月12日
import os, logging


from pymediainfo import MediaInfo
from convert.calc_md5 import calc_md5


def get_file_info(file):
    logging.basicConfig(filename='convert.log',
                        format='%(asctime)s %(levelname)s:%(message)s',
                        level=logging.DEBUG, datefmt='%Y-%m-%d %I:%M:%S')
    file_info = {}
    if not os.path.exists(file):
        print('{} --> is NOT Exists.'.format(file))
        logging.info('{} --> is NOT Exists.'.format(file))
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
