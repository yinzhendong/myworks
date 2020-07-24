import os, time, random

def renameFiles(path, prefix):
    for root, dirs, files in os.walk(path):
        count = 1
        for file in files:
            # get file postfix
            postfix = file.split('.')[-1]
            # make new file name with prefix and count.
            # example: 20200406.1.mp4
            newfilename = prefix + '.' + str(count) + '.' +postfix
            count += 1
            print(file + '-->' + newfilename)
            os.rename(os.path.join(path, file), os.path.join(path, newfilename))


# path = '/home/trent/data/temp/'
# path = '/home/trent/data/for'
path = 'D:\\temp\\'

# date = time.strftime('%Y%m%d%H%M%S')
prefix = time.strftime('%Y%m%d%H%M%S')

renameFiles(path, prefix)
