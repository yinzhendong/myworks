import xlwt, mysql.connector


def write_excel(area, date, person, team):
    """Write to Excel."""
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('个人赛成绩', cell_overwrite_ok=True)
    sheet2 = book.add_sheet('编队赛成绩', cell_overwrite_ok=True)

    person_title = [
        "排位", "所属赛区", "单位", "姓名", "手机号", "第一局成绩", "第二局成绩",
        "第三局成绩", "第四局成绩", "第五局成绩", "总成绩", "平均成绩", "最高成绩"
    ]
    team_title = [
        "排位", "所属赛区", "编队名称", "队长单位", "队长姓名", "队长手机号",
        "队长最高成绩", "队员单位", "队员姓名", "队员手机号", "队员最高成绩", "总成绩"
    ]
    #写title
    for i in range(0, len(person_title)):
        sheet1.write(0, i, person_title[i])
    for i in range(0, len(team_title)):
        sheet2.write(0, i, team_title[i])

    # 写rows

    row = 1
    for person_record in person:
        cell = 0
        for record in person_record:
            sheet1.write(row, cell, record)
            cell += 1
        row += 1

    row = 1
    for team_record in team:
        cell = 0
        for record in team_record:
            sheet2.write(row, cell, record)
            cell += 1
        row += 1

    book.save('{}赛区成绩-{}.xls'.format(area, date))


def get_area_score(area, date, count):
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
        "max_score as 最高成绩, "
        "dep as 单位 "
        "FROM person, (select @i:=0)t "
        "WHERE max_score IS NOT NULL AND area LIKE '{}%' "
        "ORDER BY 最高成绩 DESC LIMIT {}".format(area, count)
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
        "IFNULL(leader_max_score,0)+IFNULL(member_max_score,0) AS 总成绩, "
        "leader_dep as 队长单位, "
        "member_dep as 队员单位 "
        "FROM team, (select @i:=0)t "
        "WHERE  area like '{}%' AND "
        "(member_max_score IS NOT NULL OR leader_max_score IS NOT NULL) "
        "ORDER BY 总成绩 DESC LIMIT {}".format(area, count)
    )

    cursor_person_rank.execute(query_person_rank)
    cursor_team_rank.execute(query_team_rank)

    results_person_rank = cursor_person_rank.fetchall()
    results_team_rank = cursor_team_rank.fetchall()
    person_records = []
    for row in results_person_rank:
        person_record = []
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
        dep = row[12]
        person_record.append(position)
        person_record.append(area)
        person_record.append(dep)
        person_record.append(name)
        person_record.append(phone)
        person_record.append(first_score)
        person_record.append(second_score)
        person_record.append(third_score)
        person_record.append(forth_score)
        person_record.append(fifth_score)
        person_record.append(total_score)
        person_record.append(average_score)
        person_record.append(max_score)
        person_records.append(person_record)

    team_records = []
    for row in results_team_rank:
        team_record = []
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
        leader_dep = row[10]
        member_dep = row[11]
        team_record.append(position)
        team_record.append(area)
        team_record.append(team_name)
        team_record.append(leader_dep)
        team_record.append(leader_name)
        team_record.append(leader_phone)
        team_record.append(leader_max_score)
        team_record.append(member_dep)
        team_record.append(member_name)
        team_record.append(member_phone)
        team_record.append(member_max_score)
        team_record.append(team_total_score)
        team_records.append(team_record)

    cursor_person_rank.close()
    cursor_team_rank.close()
    cnx.close()

    return person_records, team_records

# 赛区列表
areas = ['全国', '安徽', '北京', '重庆', '河南', '江苏', '山西', '山东', '陕西' ]
# 成绩统计时间
date = '2019-10-6 21:00'

for area in areas:
    if area == '全国':
        continue
    else:
        result = get_area_score(area, date, 5000)
        write_excel(area, '10月18日-17时', result[0], result[1])

