import mysql.connector


def create_area_top(area, date):
    cnx = mysql.connector.connect(
        user = 'root',
        password = '',
        host = '127.0.0.1',
        database = 'ciccwargame',
    )

    cursor_person_rank = cnx.cursor(buffered=True)
    cursor_team_rank= cnx.cursor(buffered=True)

    # 查询个人赛成绩
    query_person_rank = (
        "SELECT  (@i:=@i+1)排位, "
        "area as 所属赛区, "
        "name as 姓名, "
        "phone_conv as 手机号, "
        "first_score as 第一局成绩, "
        "second_score as 第二局成绩, "
        "third_score as 第三局成绩, "
        "forth_score as 第四局成绩, "
        "fifth_score as 第五局成绩, "
        "total_score as 总成绩, "
        "average_score as 平均成绩, "
        "max_score as 最高成绩 "
        "FROM person_qualify, (select @i:=0)t "
        "WHERE max_score IS NOT NULL AND area LIKE '{}%' "
        "ORDER BY 最高成绩 DESC".format(area)
    )

    # 查询编队赛成绩
    query_team_rank = (
        "SELECT (@i:=@i+1)排位, "
        "area as 所属赛区, "
        "team_name as 编队名称, "
        "leader_name as 队长姓名, "
        "leader_phone_conv as 队长手机号, "
        "leader_max_score as 队长最高成绩, "
        "member_name as 队员姓名, "
        "member_phone_conv as 队员手机号, "
        "member_max_score as 队员最高成绩, "
        "IFNULL(leader_max_score,0)+IFNULL(member_max_score,0) AS 总成绩 "
        "FROM team_qualify, (select @i:=0)t "
        "WHERE  area like '{}%' AND "
        "(member_max_score IS NOT NULL OR leader_max_score IS NOT NULL) "
        "ORDER BY 总成绩 DESC".format(area)
    )

    cursor_person_rank.execute(query_person_rank)
    cursor_team_rank.execute(query_team_rank)

    results_person_rank = cursor_person_rank.fetchall()
    results_team_rank = cursor_team_rank.fetchall()

    # 个人成绩html
    html.write('<br><hr />')
    html.write('<h1 align=center>' + area + '--个人赛复赛</h1>')
    html.write('<h2 align=center>成绩统计时间：'+date+'</h2>')
    html.write('<table border=1 align=center>')
    html.write('<tr align=center>'
               '<th>赛区排名</th>'
                '<th>所属赛区</th>'
                '<th>姓名</th>'
                '<th>手机号</th>'
                '<th>第一局成绩</th>'
                '<th>第二局成绩</th>'
                # '<th>第三局成绩</th>'
                # '<th>第四局成绩</th>'
                # '<th>第五局成绩</th>'
                '<th>总成绩</th>'
                '<th>平均成绩</th>'
                '<th>最高成绩</th>'
                '</tr>')
    for row in results_person_rank:
        position = str(int(row[0]))
        area = row[1]
        name = row[2]
        phone = row[3]
        first_score = str(row[4]).replace('None', '')
        second_score = str(row[5]).replace('None', '')
        third_score = str(row[6]).replace('None', '')
        forth_score = str(row[7]).replace('None', '')
        fifth_score = str(row[8]).replace('None', '')
        total_score = str(row[9])
        average_score = str(int(row[10]))
        max_score = str(row[11])

        # assemble person html
        html.write('<tr align=center>')
        html.write('<td>' + position + '</td>')
        html.write('<td>' + area + '</td>')
        html.write('<td>' + name + '</td>')
        html.write('<td>' + phone + '</td>')
        html.write('<td>' + first_score + '</td>')
        html.write('<td>' + second_score + '</td>')
        html.write('<td>' + third_score + '</td>')
        html.write('<td>' + forth_score + '</td>')
        html.write('<td>' + fifth_score + '</td>')
        html.write('<td>' + total_score + '</td>')
        html.write('<td>' + average_score + '</td>')
        html.write('<td>' + max_score + '</td>')
        html.write('</tr>')
        html.write('</table>')

    # 编队成绩html
    html.write('<h1 align=center>' + area + '--编队赛</h1>')
    html.write('<h2 align=center>成绩统计时间：' + date + '</h2>')
    html.write('<table border=1 align=center>')
    html.write('<tr align=center>'
               '<th>赛区排名</th>'
               '<th>所属赛区</th>'
               '<th>编队名称</th>'
               '<th>队长姓名</th>'
               '<th>队长手机号</th>'
               '<th>队长最高成绩</th>'
               '<th>队员姓名</th>'
               '<th>队员手机号</th>'
               '<th>队员最高成绩</th>'
               '<th>总成绩</th>'
               '</tr>')
    for row in results_team_rank:
        position = str(int(row[0]))
        area = row[1]
        team_name = row[2]
        leader_name = row[3]
        leader_phone = row[4]
        leader_max_score = str(row[5]).replace('None', '')
        member_name = row[6]
        member_phone = row[7]
        member_max_score = str(row[8]).replace('None', '')
        team_total_score = str(row[9])

        # assemble team html
        html.write('<tr align=center>')
        html.write('<td>' + position + '</td>')
        html.write('<td>' + area + '</td>')
        html.write('<td>' + team_name + '</td>')
        html.write('<td>' + leader_name + '</td>')
        html.write('<td>' + leader_phone + '</td>')
        html.write('<td>' + leader_max_score + '</td>')
        html.write('<td>' + member_name + '</td>')
        html.write('<td>' + member_phone + '</td>')
        html.write('<td>' + member_max_score + '</td>')
        html.write('<td>' + team_total_score + '</td>')
        html.write('</tr>')
    html.write('</table>')
    cnx.close()


# 赛区列表
# areas = ['安徽', '北京', '重庆', '河南', '江苏', '山西', '山东', '陕西' ]
areas = ['北京']

# 成绩统计时间
date = '2019-10-18 15:00'

# write html file
with open('qualify.html', 'w', encoding='utf-8') as html:
    html.write('<!DOCtype HTML>'
               '<meta http-equiv="Content-Type" '
               'content="text/html; charset=UTF-8" />'
               '<head>'
               '<link href="./mystyle.css" rel="stylesheet" '
               'type="text/css"/>'
               '<title>复赛成绩</title>'
               '<head>'
               '<body>')

    for area in areas:
        # 生成area前num的个人赛很编队赛成绩页面
        create_area_top(area, date)

    html.write('</body>')
    html.close()
