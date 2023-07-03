import cv2 as cv

haar_cascade = cv.CascadeClassifier(r"C:\Users\eduar\OneDrive\Desktop\cse5408\haar_face-1.xml")
capture = cv.VideoCapture(r"C:\Users\eduar\OneDrive\Desktop\cse5408\face-demographics-walking.mp4")



while capture.isOpened():
    _, video = capture.read()

    gray = cv.cvtColor(video, cv.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(gray, 1.1, 4)

    
    for (x, y , w ,h) in faces:
        cv.rectangle(video, (x,y), (x+w, y+h), (0, 128, 0), 2)

    cv.imshow('video', video)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()