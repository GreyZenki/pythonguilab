
import cv2 as cv
img= cv.imread(r"C:/Users/eduar/OneDrive/Pictures/ChubbyCat-1.png")
cv.waitKey(0)

circle=cv.circle(img,(450, 150), 100, (0,0,0), 5)
cv.imshow('ChubbyCat-1',circle)

#font type
font = cv.FONT_HERSHEY_SIMPLEX 
#org
org = (250, 25)
#font scale
fontScale = 1.1
#blue 
color = (255, 0, 0)
#line thickness
thickness = 2
#cv.putText() 
img= cv.putText(img, 'Face Detected', org, font, 
                   fontScale, color, thickness, cv.LINE_AA)      
cv.imshow('ChubbyCat-1', img)
cv.waitKey(0)
