import mysql.connector


def make_last_list():
    cnx = mysql.connector.connect(
        user = 'root',
        password = '',
        host = '127.0.0.1',
        database = 'ciccwargame',
    )

    cursor_person = cnx.cursor(buffered=True)
    cursor_team = cnx.cursor(buffered=True)

    query_qualified_person = (
        "select (@rowNum:=@rowNum+1) num, area, name, phone_conv, state "
        "from person_final, (SELECT @rowNum:=0) t "
        "where state='recommend' or state='qualified' order by area, state desc"
    )

    query_qualified_team = (
        "select (@rowNum:=@rowNum+1) num, area, team_name, leader_name, "
        "leader_phone_conv, member_name, member_phone_conv, state "
        "from team_final, (SELECT @rowNum:=0) t "
        "where state='recommend' or state='qualified' order by area, state desc"
    )

    cursor_person.execute(query_qualified_person)
    cursor_team.execute(query_qualified_team)

    qualified_persons = cursor_person.fetchall()
    qualified_teams = cursor_team.fetchall()

    # 全国总决赛名单
    with open('finallist.html', 'w',encoding='utf-8') as html:
        html.write('<!DOCtype HTML>'
                   '<meta http-equiv="Content-Type" '
                   'content="text/html; charset=UTF-8" />'
                   '<head>'
                   '<link href="./mystyle.css" rel="stylesheet" '
                   'type="text/css"/>'
                   '<title>全国总决赛名单</title>'
                   '<head>'
                   '<body>')
        html.write('<br><hr />')
        html.write('<h1 align=center>全国总决赛--个人赛名单</h1>')
        html.write('<table border=1 align=center>')
        html.write('<tr align=center>'
                   '<th>序号</th>'
                   '<th>所属赛区</th>'
                   '<th>姓名</th>'
                   '<th>手机号</th>'
                   # '<th>晋级方式</th>'
                   '</tr>')
        for row in qualified_persons:
            num = str(int(row[0]))
            area = row[1]
            name = row[2]
            phone = row[3]
            # state = row[4]
            # assemble single html
            html.write('<tr align=center>')
            html.write('<td>' + num + '</td>')
            html.write('<td>' + area + '</td>')
            html.write('<td>' + name + '</td>')
            html.write('<td>' + phone + '</td>')
            # html.write('<td>' + state + '</td>')
            html.write('</tr>')
        html.write('</table>')

        # 全国总决赛编队赛名单
        html.write('<h1 align=center>全国总决赛--编队赛名单</h1>')
        html.write('<table border=1 align=center>')
        html.write('<tr align=center>'
                   '<th>序号</th>'
                   '<th>所属赛区</th>'
                   '<th>编队名称</th>'
                   '<th>队长姓名</th>'
                   '<th>队长手机号</th>'
                   '<th>队员姓名</th>'
                   '<th>队员手机号</th>'
                   # '<th>晋级方式</th>'
                   '</tr>')
        for row in qualified_teams:
            num = str(int(row[0]))
            area = row[1]
            team_name = row[2]
            leader_name = row[3]
            leader_phone = row[4]
            member_name = row[5]
            member_phone = row[6]
            # state = row[7]
            # assemble team html
            html.write('<tr align=center>')
            html.write('<td>' + num + '</td>')
            html.write('<td>' + area + '</td>')
            html.write('<td>' + team_name + '</td>')
            html.write('<td>' + leader_name + '</td>')
            html.write('<td>' + leader_phone + '</td>')
            html.write('<td>' + member_name + '</td>')
            html.write('<td>' + member_phone + '</td>')
            # html.write('<td>' + state + '</td>')
            html.write('</tr>')
        html.write('</table>')
    html.close()
    cnx.close()

make_last_list()

