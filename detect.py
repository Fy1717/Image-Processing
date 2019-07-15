import cv2

# Yüz için Default bir xml Haarcascade dosyası kullanıyorum
defaultCizim = "haarcascade_frontalface_default.xml"
yuzCascade = cv2.CascadeClassifier(defaultCizim)

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    yuz = yuzCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Yüzün 4 noktasına göre çevrelenmesı
    for (x, y, w, h) in yuz:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "FY", (x+50 , y+120 ), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)

    # Pencereye başlık atıyorum
    cv2.imshow('FY-Image Processing', frame)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

# Fonksiyonları çalıştırıyorum
video_capture.release()
cv2.destroyAllWindows()
