import xlwt, mysql.connector


def write_excel(person, team):
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

    book.save('全国总决赛名单.xls')


def get_area_final_list():
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
        "select (@i:=@i+1)排位,area 所属赛区,name 姓名,phone 手机号,"
        "max_score 晋级赛成绩,dep 单位,state 晋级方式 "
        "from person_final, (select @i:=0)t "
        "where state='recommend' or state='qualified' "
        "order by field(area,'北京分赛区','重庆分赛区','河南分赛区','湖南分赛区',"
        "'安徽分赛区','山东分赛区','江苏分赛区','浙江分赛区','湖北分赛区','广西分赛区',"
        "'山西分赛区','陕西分赛区','吉林分赛区')"
    )

    # 查询编队赛成绩
    query_team_rank = (
        "SELECT (@i:=@i+1)排位,area 所属赛区,team_name 编队名称,leader_name 队长姓名,"
        "leader_phone 队长手机号,leader_max_score 队长晋级赛成绩,member_name 队员姓名,"
        "member_phone 队员手机号,member_max_score 队员晋级赛成绩,"
        "IFNULL(leader_max_score,0)+IFNULL(member_max_score,0) 总成绩,"
        "leader_dep 队长单位,member_dep 队员单位,state 晋级方式 "
        "FROM team_final,(select @i:=0)t "
        "WHERE state='recommend' or state='qualified' "
        "order by field(area,'北京分赛区','重庆分赛区','河南分赛区','湖南分赛区',"
        "'安徽分赛区','山东分赛区','江苏分赛区','浙江分赛区','湖北分赛区','广西分赛区',"
        "'山西分赛区','陕西分赛区','吉林分赛区')"
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
    result = get_area_final_list()
    write_excel(result[0], result[1])

main()
