import subprocess
import os


from convert.file_info import get_file_info


def ffmpeg_convert_video_to_mp4(original_file, transcode_file):
    file_info = get_file_info(original_file)
    convert_command = (
            "ffmpeg " + ' -i ' + original_file + ' -c:v libx264' + ' -strict -2'
            + ' -s ' + str(file_info['width']) + 'x'
            + str(file_info['height']) + ' -b:v ' + str(file_info['vb'])
            + ' -b:a ' + str(file_info['ab']) + ' -y ' + transcode_file
    )
    print(convert_command)

    if not os.path.exists(os.path.split(transcode_file)[0]):
        os.makedirs(os.path.splitext(transcode_file)[0])

    a = subprocess.run(convert_command, shell=True)
    if a.returncode == 0:
        return True
    else:
        return False
