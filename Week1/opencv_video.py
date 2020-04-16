import cv2

cap = cv2.VideoCapture('test.mp4')
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
      break
    cv2.imshow('',frame)
       
    cv2.waitKey(10)  & 0xFF
    
cap.release()
cv2.destroyAllWindows()
