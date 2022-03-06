import cv2
import  numpy as np

img = cv2.imread("quest2.png")
gbr = cv2.imread("result2.png")
blur = cv2.medianBlur(img,5)
(T, threshInv) = cv2.threshold(blur, 85, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((20,20),np.uint8)
opening = cv2.morphologyEx(threshInv, cv2.MORPH_OPEN, kernel)

cv2.imshow("Result Soal", gbr)
cv2.imshow("Gambar Asli", img)
cv2.imshow("Hasil Gambar2", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
