import subprocess
import os

# ffmpeg.exe -i d:\1.mp4 -ss 00:02:00 -frames:v 1 -y 1.jpg

def getPic(file):
    command = (
        'C:\\Users\\Administrator\\Downloads\\'
        'ffmpeg-4.3.1-2020-11-08-full_build\\bin\\ffmpeg.exe' +
        ' -i ' + file + ' -ss 00:01:00 ' + '-frames:v 1 ' + '-y '
        + file +'.jpg'
    )
    print(command)
    subprocess.run(command, shell=True)



def getFile(path):
    file_path = []
    for root, dirs, files in os.walk(path):
        for file in files:
            # print(file)
            file_path.append(os.path.join(path, file))
    return file_path


file_path = getFile('d:\\clips')
# getPic('d:\\clips\\20200910214320.100.mp4')

for file in file_path:
    getPic(file)