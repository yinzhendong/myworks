#### 报名信息导入数据库执行过程
1. 执行完excel报名新增信息导入到person、person_all、team表后

#### 整理华戍成绩为个人赛及编队成绩
1. 将华戍导出的成绩整理成excel表导入到数据库中的score表中
2. 执行check_score.py检查是否报名表中存在的手机号重复人员,以及是否存在score表中有成绩,
但是人员信息中没有的情况
3. 执行更新update_score.py
4. 执行top.py根据需要生成初赛全国及各赛区排位，参数为date、排位数量
5. 执行writeToExcel.py按赛区导出成绩的excel表格

#### 查找人员信息
1. 执行find_someone.py，参数name、phone

#### 报名信息整理成华戍要求表格
1. 使用enroll数据库
2. 分别将个人赛、编队赛报名信息导入person、team表中
3. 执行convert_single.py从forimported表中导出个人赛华戍格式
4. 执行convert_team.py从forimported表中导出编队赛华戍格式

