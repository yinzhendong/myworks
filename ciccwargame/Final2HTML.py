import mysql.connector


def create_final_qualified(date):
    cnx = mysql.connector.connect(
        user = 'root',
        password = '',
        host = '127.0.0.1',
        database = 'ciccwargame',
    )

    cursor_qualified_person = cnx.cursor(buffered=True)
    cursor_qualified_team = cnx.cursor(buffered=True)

    query_qualified_person = (
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
        "FROM person_final, (select @i:=0)t "
        "WHERE max_score IS NOT NULL and (state='' or state is null)"
        "ORDER BY 最高成绩 DESC"
    )

    query_qualified_team = (
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
        "FROM team_final, (select @i:=0)t "
        "WHERE (member_max_score IS NOT NULL OR leader_max_score IS NOT NULL) "
        "and (state='' or state is null)"
        "ORDER BY 总成绩 DESC"
    )

    cursor_qualified_person.execute(query_qualified_person)
    cursor_qualified_team.execute(query_qualified_team)

    results_qualified_persons = cursor_qualified_person.fetchall()
    results_country_teams = cursor_qualified_team.fetchall()

    # 个人赛成绩
    with open('final.html', 'w',encoding='utf-8') as html:
        html.write('<!DOCtype HTML>'
                   '<meta http-equiv="Content-Type" '
                   'content="text/html; charset=UTF-8" />'
                   '<head>'
                   '<link href="./mystyle.css" rel="stylesheet" '
                   'type="text/css"/>'
                   '<title>全国晋级赛成绩排名</title>'
                   '<head>'
                   '<body>')
        html.write('<br><hr />')
        html.write('<h1 align=center>全国总决赛晋级赛--个人赛成绩</h1>')
        html.write('<h2 align=center>成绩统计时间：' + date + '</h2>')
        html.write('<table border=1 align=center>')
        html.write('<tr align=center>'
                   '<th>排名</th>'
                   '<th>所属赛区</th>'
                   '<th>姓名</th>'
                   '<th>手机号</th>'
                   '<th>第一局成绩</th>'
                   '<th>第二局成绩</th>'
                   '<th>第三局成绩</th>'
                   '<th>第四局成绩</th>'
                   '<th>第五局成绩</th>'
                   '<th>总成绩</th>'
                   '<th>平均成绩</th>'
                   '<th>最高成绩</th>'
                   '</tr>')
        for row in results_qualified_persons:
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

            # assemble single html
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

        # 编队赛成绩
        html.write('<h1 align=center>全国总决赛晋级赛--编队赛成绩</h1>')
        html.write('<h2 align=center>成绩统计时间：' + date + '</h2>')
        html.write('<table border=1 align=center>')
        html.write('<tr align=center>'
                   '<th>排名</th>'
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
        for row in results_country_teams:
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
    html.close()
    cnx.close()


