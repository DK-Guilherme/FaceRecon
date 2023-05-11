import cv2 as cv #opencv permite controlar nossa webcam e carregar a imagem da webcam
import mediapipe as mp #vai permitir fazer o reconhecimento da nossa imagem

#incializar o opencv e mediapipe
webcam = cv.VideoCapture(0)
face_reconize_slt = mp.solutions.face_detection
face_reconize = face_reconize_slt.FaceDetection()
draw = mp.solutions.drawing_utils

while True:
  #Ler as inforamações da webcam
  checker, frame = webcam.read()
  if not checker:
    break
 
  #reconhecer os rostos que tem ali dentro
  face_list = face_reconize.process(frame)

  if face_list.detections:
    for rostos in face_list.detections:
      #desenhar rostos na imagem
      draw.draw_detection(frame, rostos)

      cv.imshow("Face on WebCam", frame)

      #Quando apertar "Q" sair do loop
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()
