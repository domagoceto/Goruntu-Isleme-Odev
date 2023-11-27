import cv2
import numpy as np


img = cv2.imread("pirinc.jpg")




img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


_, maske = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY) 


boyut = np.ones((5, 5), np.uint8)
maske1 = cv2.morphologyEx(maske, cv2.MORPH_OPEN, boyut, iterasyon=2)

maske1_copy = cv2.morphologyEx(maske, cv2.MORPH_OPEN, boyut, iterasyon=2)



contours, _ = cv2.findContours(maske1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


pirinc_Sayisi = len(contours)




contours, _ = cv2.findContours(maske1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


pirinc_Sayisi = len(contours)


for i, contour in enumerate(contours, 1):
    cv2.drawContours(maske1, [contour], -1, (0, 255, 0), 2)
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.putText(maske1, f"{i}", (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 8)




yeniResim = cv2.resize(img, (800,700))
yeniCikti = cv2.resize(maske1, (800,700))

cv2.imshow("resim",yeniResim)
cv2.imshow("Çıktı", yeniCikti)

cv2.waitKey()
cv2.destroyAllWindows()