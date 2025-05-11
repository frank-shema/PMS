import cv2
import time

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
time.sleep(2)  # Allow camera to initialize

if not cap.isOpened():
    print("Cannot open camera")
    exit()

ret, frame = cap.read()
print("Frame read:", ret)

cap.release()
