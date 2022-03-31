import cv2
import face_recognition
import os

cam = cv2.VideoCapture(0)

cv2.namedWindow('compare image')

ret, frame = cam.read()
if not ret:
  print('falled to grab frame!')
  cv2.destroyAllWindows()
else:
  cv2.imshow('capture photo',frame) 
  img_name = 'opencv_compare_image.jpg'
  cv2.imwrite(img_name, frame)

  photo_one = face_recognition.load_image_file('opencv_frame_image.jpg')
  photo_two = face_recognition.load_image_file('opencv_compare_image.jpg')

  photo_one_encoding = face_recognition.face_encodings(photo_one)[0]
  photo_two_encoding = face_recognition.face_encodings(photo_two)[0]

  results = face_recognition.compare_faces([photo_one_encoding], photo_two_encoding)

  if results == [True]:
    print('Acesso liberado')
  else: 
    print('Acesso negado') 

os.remove('opencv_compare_image.jpg')    


  











