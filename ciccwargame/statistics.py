import mysql.connector
import time
import xlwt
import logging

# log into file 'statistics.log'
logging.basicConfig(filename='statistics.log',
                    format='%(asctime)s %(levelname)s:%(message)s',
                    level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')
logging.info('statistics starting...')


cnx = mysql.connector.connect(
    user = 'root',
    password = '',
    host = '127.0.0.1',
    database = 'ciccwargame',
)
cursor = cnx.cursor()


def make_statistics(tb_name, area):
    """
    统计所有赛区的个人和编队报名的总数量
    """
    sql = (
        "select count(*) from {} where area like '{}%'"
    ).format(tb_name, area)
    cursor.execute(sql)
    return cursor.fetchall()


# 赛区列表
areas = ['安徽', '北京', '重庆', '河南', '江苏', '山西', '山东', '陕西','吉林',
         '浙江', '湖北', '广西']
tb_names = ['person_final', 'team_final']
date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

# 统计各赛区的个人和编队赛报名数据
for area in areas:
    logging.info('---------------------------')
    logging.info('{}赛区报名情况：'.format(area))
    for tb_name in tb_names:
        results = make_statistics(tb_name, area)
        if tb_name == 'person':
            logging.info('个人赛报名人数：{}'.format(results[0][0]))
        else:
            logging.info('编队赛报名人数：{}'.format(results[0][0]))

# write_excel(areas, date.split(' ')[0], 2234)

cursor.close()
cnx.close()
