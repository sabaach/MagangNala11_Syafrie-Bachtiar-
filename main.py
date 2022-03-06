import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("result1.png")
gbr = cv2.imread("quest1.png")

blur = cv2.medianBlur(gbr,5)
kernel = np.ones((3,3), np.uint8)
erosion = cv2.erode(blur, kernel, iterations=1)
#cell = cv2.cvtColor(gbr,cv2.COLOR_BGR2GRAY)
#blur = cv2.GaussianBlur(cell, (7,7), 0)
#ret, th = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
(T, threshInv) = cv2.threshold(erosion, 27, 255, cv2.THRESH_BINARY_INV)
newblur = cv2.medianBlur(threshInv,5)
#newblur = cv2.GaussianBlur(threshInv, (7,7), 0)
#ewblur2 = cv2.medianBlur(newblur,5)
edges = cv2.Canny(newblur,50,255)
cv2.imshow('Final Gambar',edges)

cv2.imshow("result1", img)
cv2.imshow('Gambar Jernih', erosion)
cv2.imshow("Quest1", gbr)
cv2.imshow("Treshold Binary Invers", threshInv)
cv2.imshow("Treshold Binary di blur", newblur)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.imshow(cell, cmap="gray")
#plt.show()
#edges = cv2.Canny(blur,100,200)
#cv2.imshow('CannyEdge',edges)
#cv2.waitKey(0)
#cv2.destroyAllWindows()





