## 长安大学转码替换
> 转码状态说明  
100 不需要转码  
0 等待转码  
1 正在转码  
2 转码成功  
3 转码失败  
4 已加入转码队列  
#### 数据库授权
```
grant all on *.* to root@'%' identified by 'password' with grant option;
flush privileges;
```
#### bmc数据库说明
* 涉及的表为:boful_file和transcode_file
* program的serial文件放在boful_file表里，表中的transcode_state字段标识转码状态
* 表transcode_file通过boful_file_id和表boful_file关联，用来存放转码的文件信息，
如果设置了多码率，表中boful_file_id多对表boful_file的id是多对一的关系
#### 处理步骤
（暂时只处理原始码率转码，多码率转码后续增加; 由于原来的业务逻辑比较复杂，只处理原转码程序
在队列卡死的情况）  
* 查询bmc数据库取得所有转码失败的文件信息（转码状态为3）  
`SELECT * FROM boful_file WHERE transcode_state=3`

* 调用新的转码模块，进行转码，并更新boful_file表和transcode_file表, 剩下的转码同步问题，
交由原程序处理
```
SELECT * FROM boful_file b LEFT JOIN transcode_file s ON b.id=s.boful_file_id WHERE b.file_hash='84FCDF40C2910DE3DB9F9327B4E34227'
SELECT * FROM serial s LEFT JOIN program p ON s.program_id=p.id WHERE s.file_hash='84FCDF40C2910DE3DB9F9327B4E34227'
SELECT b.file_path, t.file_path, t.transcode_state FROM boful_file b LEFT JOIN transcode_file t ON b.id=t.boful_file_id WHERE b.transcode_state=3
```
#### ?
* 怎么判断原转码服务卡死  
  通过ffmpeg状态？

#### 安装环境
* 安装openssl-devel  
`yum install openssl-devel -y`
* 安装Python(Python版本3.6.8)  
```
tar zxvf Python-3.6.8.tgz
cd Python-3.6.8
./configure --prefix=/usr/local --with-ssl
make && make altinstall
```
运行以上命令后，你可以在目录/usr/local/bin/python3.6 看到新编译的环境。
PS： 这里我们使用的是make altinstall，如果使用make install，
你将会看到在系统中有两个不同版本的Python在/usr/bin/目录中。
这将会导致很多问题，而且不好处理。  
* 创建virtualenv  
`./python3.6 -m venv /home/boful/convert/venv`
* 安装pymediainfo  
`pip install pymediainfo`
* 安装mysql-connector  
`pip install mysql-connector`

#### 测试方法
* 备份bmc数据库，然后用备份的数据库进行测试，以免发生问题
