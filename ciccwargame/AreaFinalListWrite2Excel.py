import xlwt, mysql.connector


def write_excel(area, person, team):
    """Write to Excel."""
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('个人赛名单', cell_overwrite_ok=True)
    sheet2 = book.add_sheet('编队赛名单', cell_overwrite_ok=True)

    person_title = [
        "序号", "所属赛区", "单位", "姓名", "手机号", "晋级赛最高成绩", "晋级方式"
    ]
    team_title = [
        "序号", "所属赛区", "编队名称", "队长单位", "队长姓名", "队长手机号",
        "队长晋级赛最高成绩", "队员单位", "队员姓名", "队员手机号", "队员晋级赛最高成绩",
        "总成绩", "晋级方式"
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

    book.save('全国总决赛名单-' + area + '.xls')


def get_area_final_list(area):
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
        "phone as 手机号, "
        "max_score as 晋级赛最高成绩, "
        "dep as 单位, "
        "state as 晋级方式 "
        "FROM person_final, (select @i:=0)t "
        "WHERE state='recommend' and area like '{}%' "
        "ORDER BY state desc, max_score desc".format(area)
    )

    # 查询编队赛成绩
    query_team_rank = (
        "SELECT (@i:=@i+1)排位, "
        "area as 所属赛区, "
        "team_name as 编队名称, "
        "leader_name as 队长姓名, "
        "leader_phone as 队长手机号, "
        "leader_max_score as 队长晋级赛最高成绩, "
        "member_name as 队员姓名, "
        "member_phone as 队员手机号, "
        "member_max_score as 队员晋级赛最高成绩, "
        "IFNULL(leader_max_score,0)+IFNULL(member_max_score,0) AS 总成绩, "
        "leader_dep as 队长单位, "
        "member_dep as 队员单位, "
        "state as 晋级方式 "
        "FROM team_final, (select @i:=0)t "
        "WHERE state='recommend' and area like '{}%' "
        "ORDER BY state desc, 总成绩 DESC".format(area)
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
        max_score = str(row[4])
        dep = row[5]
        state = row[6]
        person_record.append(position)
        person_record.append(area)
        person_record.append(dep)
        person_record.append(name)
        person_record.append(phone)
        person_record.append(max_score)
        person_record.append(state)
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
        state = row[12]
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
        team_record.append(state)
        team_records.append(team_record)

    cursor_person_rank.close()
    cursor_team_rank.close()
    cnx.close()

    return person_records, team_records


def main():
    areas = ['安徽', '北京', '重庆', '河南', '江苏', '山西', '山东', '陕西', '湖北',
             '湖南', '浙江', '吉林', '广西', ]
    for area in areas:
        result = get_area_final_list(area)
        write_excel(area, result[0], result[1])

main()
