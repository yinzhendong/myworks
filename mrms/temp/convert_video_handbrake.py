import subprocess


from utils.get_video_info import get_video_info

file = '/home/trent/workspace/learning/work/1.avi'

file_info = get_video_info(file)
# print(file_info)

convert_command = "HandBrakeCLI -e x264" \
                  + ' -w ' + str(file_info['width']) \
                  + ' -l ' + str(file_info['height']) \
                  + ' -b ' + str(int(file_info['vb']/1000)) \
                  + ' -B ' + str(int(file_info['ab']/1000)) \
                  + ' -i ' + file \
                  + ' -o ' + file + '.mp4'
# print(convert_command)
a = subprocess.run(convert_command, shell=True, stdout=subprocess.PIPE)
if a.returncode == 0:
    print("Encode Successful!")
else:
    rint("Encode False!")
