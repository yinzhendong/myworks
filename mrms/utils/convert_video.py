import subprocess
import os


from mrms.utils.file_info import get_file_info

# base_dir = '/home/trent/data/workspace/PycharmProjects/python_works/mrms/'
# file = os.path.join(base_dir, '/resources/video/1.avi')


def ffmpeg_convert_video_to_mp4(file):
    file_info = get_file_info(file)
    convert_command = (
            "ffmpeg " + ' -i ' + file + ' -c:v libx264' + ' -strict -2'
            + ' -s ' + str(file_info['width']) + 'x'
            + str(file_info['height']) + ' -b:v ' + str(file_info['vb'])
            + ' -b:a ' + str(file_info['ab']) + ' -y ' + file + '.mp4'
    )
    print(convert_command)

    a = subprocess.run(convert_command, shell=True)
    if a.returncode == 0:
        # print("Encode Successful!")
        return True
    else:
        # print("Encode False!")
        return False
# ffmpeg_convert_video_to_mp4(
#     '/home/trent/data/workspace/PycharmProjects/python_works/mrms/resources/'
#     'video/1.avi'
# )
