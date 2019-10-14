import hashlib
import os


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
