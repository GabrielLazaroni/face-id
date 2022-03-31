
import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow('capture photo')

ret, frame = cam.read()
if not ret:
  print('falled to grab frame!')
  cv2.destroyAllWindows()
else:   
  cv2.imshow('capture photo',frame) 
  img_name = 'opencv_frame_image.jpg'
  cv2.imwrite(img_name, frame)
  print('{} written!'.format(img_name))
  
cam.release()

cv2.destroyAllWindows()


