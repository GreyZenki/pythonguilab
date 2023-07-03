
import cv2 as cv 
img= cv.imread(r"C:/Users/eduar/OneDrive/Pictures/ChubbyCat-1.png")


#parameter values
threshold_L = 100 
threshold_U = 200

#gray
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#blur with gray
blur = cv.GaussianBlur(gray, (7,7), cv.BORDER_DEFAULT)


#shows images
#original
cv.imshow('ChubbyCat-1',img)
cv.waitKey(0)

#gray
cv.imshow('Gray',gray)
cv.waitKey(0)
#blur w/ gray
cv.imshow('Blur', blur)
cv.waitKey(0)

#Canny Edge filter
#edge with blur w/gray
edge = cv.Canny(blur, threshold_L, threshold_U)
cv.imshow('edge_b', edge)
#edge no blur or gray
edge = cv.Canny(img, threshold_L, threshold_U)
cv.imshow('edge', edge)
cv.waitKey(0)