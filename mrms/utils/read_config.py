import configparser


# 读取配置文件中的‘path’section
def get_base_dir():
    config_file = 'conf/config.ini'
    config_obj = configparser.ConfigParser()
    config_obj.read(config_file, encoding='utf-8')
    sections = config_obj.sections()
    items = config_obj.items('path')
    return  dict(items)['base_dir']

def get_db_con():
    config_file = 'conf/config.ini'
    config_obj = configparser.ConfigParser()
    config_obj.read(config_file, encoding='utf-8')
    sections = config_obj.sections()
    items = config_obj.items('database')
    return dict(items)
