# source ~/env/bin/activate in command line
# Tạo option chọn vertical hoặc horizontal

import cv2
import time
import os
import datetime

t0 = time.time()
y_dynamic = 0

video = cv2.VideoCapture(0)
_,frame1 = video.read()
x1 = frame1.shape[1]
final_image = frame1[y_dynamic:y_dynamic+1,0:x1]

while True:
    ret, frame = video.read()
    if ret:
        if (time.time() - t0 > 0.01): 
            print(time.time() - t0)
            y_dynamic = y_dynamic + 1
            if y_dynamic == frame1.shape[0]:
                break
            final_image = cv2.vconcat([final_image,frame[y_dynamic:y_dynamic+1,0:x1]])
            t0 = time.time()
        cv2.line(frame, (0, y_dynamic), (x1, y_dynamic), (255, 0, 0), thickness=2)
        image2show = cv2.vconcat([final_image,frame[y_dynamic:, 0:x1]])
        cv2.imshow("IPCam",image2show)
    if cv2.waitKey(1) == ord("q"):
        break

x = datetime.datetime.now()
strnow = x.strftime("%Y%m%d%H%M%S")
cv2.imwrite(f"{strnow}.jpg",final_image)


video.release()
cv2.destroyAllWindows()
