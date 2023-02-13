
import cv2

video_capture = cv2.VideoCapture(0) # 0 means device camera
# video_capture is an instance of the VideoCapture Class

haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    # Capture frame-by-frame
    isTrue, frames = video_capture.read()
    # isTrue will hold boolean value if the frame was accessed or not
    # frame will hold the each frame of the video in loop 

    # coverting each fram in the video to grayscale
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.rectangle(frames, (x, y), (x + 40, y - 15), (0, 255, 0), -1)
        cv2.putText(frames, "FACE", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))

    # Display the resulting frame
    cv2.imshow('Video', frames)

    # to break the loop by pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()