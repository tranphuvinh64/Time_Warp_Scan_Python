# source ~/env/bin/activate in command line
# Tạo option chọn vertical hoặc horizontal

import cv2
import time
import os
import datetime

t0 = time.time()
x_dynamic = 0

video = cv2.VideoCapture(0)
_,frame1 = video.read()
y1 = frame1.shape[0]
final_image = frame1[0:y1,x_dynamic:x_dynamic + 1]

while True:
    ret, frame = video.read()
    if ret:
        if (time.time() - t0 > 0.01): 
            print(time.time() - t0)
            x_dynamic = x_dynamic + 1
            if x_dynamic == frame1.shape[1]:
                break
            final_image = cv2.hconcat([final_image,frame[0:y1, x_dynamic:x_dynamic+1]])
            t0 = time.time()
        cv2.line(frame,(x_dynamic,0), (x_dynamic, y1), (255, 0, 0), thickness=2)
        image2show = cv2.hconcat([final_image,frame[0:y1, x_dynamic:]])

        cv2.imshow("IPCam",image2show)
    if cv2.waitKey(1) == ord("q"):
        break

x = datetime.datetime.now()
strnow = x.strftime("%Y%m%d%H%M%S")
cv2.imwrite(f"{strnow}.jpg",final_image)


video.release()
cv2.destroyAllWindows()
