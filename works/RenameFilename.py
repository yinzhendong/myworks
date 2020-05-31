import os, shutil


path = 'C:\\Users\\Administrator\\Downloads\\傲骨贤妻第2季\\'
# path = 'D:\\爱，死亡与机器人第1季\\'

for root, dirs, files in os.walk(path):
    for file in files:
        # print(file.split('.'))
        new_name = file.split('.')[4]
        extend = file.split('.')[-1]
        # print(new_name + '.' + extend)
        new_filename = new_name + '.' + extend
        # print(os.path.join(path, new_filename))
        print(os.path.join(path, file) + '-->' + os.path.join(path, new_filename))
        os.rename(os.path.join(path, file), os.path.join(path, new_filename))
