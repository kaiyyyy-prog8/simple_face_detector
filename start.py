import cv2
import os
import argparse
from imutils.video import VideoStream
import imutils # install this and picamera
import time

# create a directory if it doesnt exist, as a location to store captured photos
def mk_dir(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

ap = argparse.ArgumentParser()
# use the command python3 THIS_FILE_NAME --picamera 0 to use a webcam
ap.add_argument("-p", "--picamera", type=int, default=1,help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())

# initialize the video stream and allow the camera sensor to warmup
video_capture = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

# load the provided haar cascadeclassier for faces
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# set a counter for the saved image
count = 0

#as the function declared at the top
mk_dir("suspects/")

# start collecting facial images
while(True):
    
    # read video frames
    image_frame = video_capture.read()

    # convert to grayscale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
    
    # you can find out more about how the 2nd and 3rd arguments affect the speed and accuracy
    # on the OpenCV documentation. 1.3 and 5 are the default tutorial values!
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
    # display the video frame, with bounded rectangle on the person's face
    cv2.imshow('frame', image_frame)
    
    # each face will give you a x y w h, where 0,0 is the top left
    for (x,y,w,h) in faces:

        # draw a rectangle around the detected face
        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
        # show the frame with the drawn image
        cv2.imshow('frame', image_frame)
        
        # give an allowance of extra allowance for each direction to crop. Checks for overshots for a 720x480 capture
        # change allowance to 0 to not use this feature
        # this is to prevent overcropping of faces
        allowance = 20
        if(y-allowance > 0 and y + allowance < 720 and x - allowance > 0 and x + allowance < 480):
            # increase count of images taken
            count += 1
            print("suspect image " + str(count))
            crop = image_frame[y-allowance:y+h+allowance,x-allowance:x+w+allowance]
            
            # save captured face
            cv2.imwrite("suspects/suspect " + str(count) + ".jpg", crop)

            # prevent too many captures of the same person by sleeping
            print("sleeping...")
            time.sleep(2)
            print("ready to capture")
    
        else:
            continue 
    
    # press q to quit. This may not work on remote connection
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
video_capture.stop()
cv2.destroyAllWindows()
