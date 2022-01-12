import os, shutil


def move_files(src_path, dst_path):
    """Move src_path all files to dst_path and rename the conflict files."""

    # Check src_path and dst_path is exists.
    if not os.path.exists(src_path):
        print("src_path --> {} --> is not exists.".format(src_path))
        return
    if not os.path.exists(dst_path):
        print("src_path is not exists.")
        return

    # Get all files in src_path
    x = 1
    for root, dirs, files in os.walk(src_path):
        for file in files:
            # absolute src_path file
            src_abs_file = os.path.join(root, file)

            # absolute dst_path file
            dst_abs_file = os.path.join(dst_path, file)

            if not os.path.exists(dst_abs_file):
                print('{} --> is not in dst_path'.format(dst_abs_file))
                shutil.move(src_abs_file, dst_abs_file)
            else:
                rename_dst_abs_file = os.path.splitext(
                    dst_abs_file)[0] + '_(' + str(x) + ')_' + os.path.splitext(
                    dst_abs_file)[1]
                x += 1
                print(rename_dst_abs_file)
                shutil.move(src_abs_file, rename_dst_abs_file)


# src_path = '/home/trent/data/download/'
# src_path = 'D:\\download\\'
src_path = 'D:\\clips\\'
# src_path = '/home/trent/data/tmp/'
# dst_path = '/home/trent/data/temp/'
dst_path = 'D:\\temp\\'
move_files(src_path, dst_path)
