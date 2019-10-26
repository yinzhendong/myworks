import os, logging


def delete_empty_directories(path):
    """Delete empty directories in the given path."""

    # log into file 'DeleteDirs.log'
    logging.basicConfig(filename='DeleteDirs.log',
                        format='%(asctime)s %(levelname)s:%(message)s',
                        level=logging.DEBUG, datefmt='%Y-%m-%d %I:%M:%S')
    logging.info("Delete the empty dir in --> '{}'.".format(path))

    # Check path is exists.
    if not os.path.exists(path):
        print('Path --> {} --> not exists.'.format(path))
        logging.info('Path --> {} --> not exists.'.format(path))

    # remove the empty dirs.
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            abs_dir = os.path.join(root, dir)
            if not os.listdir(abs_dir):
                logging.info('Delete {} successful.'.format(abs_dir))
                os.removedirs(abs_dir)
    logging.info("There is no empty directories in --> {}".format(path))
    print("There is no empty directories in --> {}".format(path))

path = "/home/trent/data/download/"

delete_empty_directories(path)
