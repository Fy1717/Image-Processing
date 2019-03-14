import cv2
import numpy as np


kamera = cv2.VideoCapture(0)

while True:
    ret,kare = kamera.read()
    gri_kare =cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    nesne = cv2.imread("teldeneme2.jpg",0)

    # w = genişlik  h = yükseklik
    w,h=nesne.shape

    print("konum")
    print("\n\n")

    res= cv2.matchTemplate(gri_kare,nesne,cv2.TM_CCOEFF_NORMED)
    esik_degeri= 0.60
    loc = np.where(res>esik_degeri)
    for n in zip(*loc[::-1]):
        cv2.rectangle(kare,n,(n[0]+h,n[1]+w),(0,255,0),1)
        cv2.putText(kare,"Nesne",(n[0]+0,n[1]+110),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)

        # print(n+"\n")   string değil

        # genişlik ve yükseklik değerlerini yazdıralım
        print("konum\n")
        print(n[0])
        print(n[1])
        # print(str(loc))

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # ANLAMLI İKİLİ DEĞERLER ALIYORUM
        # print(min_loc)
        # print("\n")
        # print(max_loc)
        # print("\n")

    cv2.imshow("ekran",kare)

    #time.sleep(1)
    if cv2.waitKey(25) & 0XFF == ord("q"):
        break
kamera.release()