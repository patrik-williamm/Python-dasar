
#install library openCv
import cv2

#read img
img = imread('test.jpg')

#show img
cv2.imshow('img 01',img)

#save img
cv.imwrite('img 01_save', img)

#menunda windows terdestoy
cv2.waitKey(0)

#mendestroy windows
cv2.destroyAllWindows()
