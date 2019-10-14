#### 一、 转码程序处理流程
1. convert.py 程序从数据库中读取所有等待转码的文件，包含视频、音频、文档
2. convert.py 程序调用utils.convert_queue.py，处理转码队列
3. convert_queue.py 调用utils.convert_video.py 对视频进行转码

#### 二、转码状态说明
对应bmc数据库中的boful_file和transcode_file表中的transcode_state字段

#### 三、转码标志位说明
0 不需转码  
1 转码成功  
2 等待转码  
3 转码成功  
4 转码失败  