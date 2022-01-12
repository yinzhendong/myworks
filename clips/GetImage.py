import cv2


vc = cv2.VideoCapture('D:\\1.mp4')  # 读取视频文件
c = 0
print("Starting...")

if vc.isOpened():  # 判断是否正常打开
    print("Open video file OK.")
    rval, frame = vc.read()
else:
    rval = False
    print("Open video file Failed.")

count = 0

while rval:
    rval, frame = vc.read()
    if (count == 1000):
        cv2.imwrite('1.jpg', frame)  # 存储为图像
        break
    count = count + 1
    print(count)

vc.release()
print("Done...")
