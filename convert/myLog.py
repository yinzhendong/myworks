import logging


def my_logging():
    logging.basicConfig(filename='convert.log',
                        format='%(asctime)s %(levelname)s:%(message)s',
                        level=logging.DEBUG, datefmt='%Y-%m-%d %I:%M:%S')