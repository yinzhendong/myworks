import xlwt, mysql.connector


def write_excel(person):
    """Write to Excel."""
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('积分排位', cell_overwrite_ok=True)
    person_title = ["排位", "队伍名称", "积分", "局分", "已比赛场次"]
    #写title
    for i in range(0, len(person_title)):
        style = xlwt.XFStyle()
        al = xlwt.Alignment()
        al.horz = 0x02
        al.vert = 0x01
        font = xlwt.Font()
        font.bold = 20*11
        style.alignment = al
        style.font = font
        sheet1.write(0, i, person_title[i], style)
    # 写rows
    row = 1
    for person_record in person:
        style = xlwt.XFStyle()
        al = xlwt.Alignment()
        al.horz = 0x02
        al.vert = 0x01
        style.alignment = al
        cell = 0
        for record in person_record:
            sheet1.write(row, cell, record, style)
            cell += 1
        row += 1
    book.save('智能博弈赛总决赛排位.xls')


def get_area_final_list():
    cnx = mysql.connector.connect(
        user = 'root',
        password = '',
        host = '127.0.0.1',
        database = 'moziai2020',
    )

    cursor_person_rank = cnx.cursor(buffered=True)

    # 查询个人赛成绩
    query_person_rank = (
        "SELECT (@i:=@i+1) AS 排位, a.* FROM (SELECT @i:=0) AS t "
        "JOIN (SELECT team_name AS 编队名称, SUM(points) AS 积分, "
        "SUM(score) AS 局分, COUNT(*) AS 已比赛场次 FROM score "
        "GROUP BY team_name ORDER BY 积分 DESC, 局分 DESC) AS a"
    )

    cursor_person_rank.execute(query_person_rank)

    results_person_rank = cursor_person_rank.fetchall()
    person_records = []
    for row in results_person_rank:
        person_record = []
        position = str(int(row[0]))
        team_name = row[1]
        points = row[2]
        score = row[3]
        match_times = row[4]
        person_record.append(position)
        person_record.append(team_name)
        person_record.append(points)
        person_record.append(score)
        person_record.append(match_times)
        person_records.append(person_record)

    cursor_person_rank.close()
    cnx.close()

    return person_records


def main():
    result = get_area_final_list()
    write_excel(result)

main()
