import cv2
import imutils
   
# Initializing the HOG person

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
   
cap = cv2.VideoCapture('2.mp4')
   
while cap.isOpened():
    # Reading the video stream
    ret, image = cap.read()
    if ret:
        image = imutils.resize(image, width=min(400, image.shape[1]))
        (regions, _) = hog.detectMultiScale(image,winStride=(8, 8),padding=(8, 8),scale=1.05)
        # Drawing the regions in the 
        # Image
        for (x, y, w, h) in regions:
            cv2.rectangle(image, (x, y),(x + w, y + h), (0, 0, 255), 2)
            cv2.putText(image, 'People', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
        # Showing the output Image
        cv2.imshow("Image", image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
  
cap.release()
cv2.destroyAllWindows()