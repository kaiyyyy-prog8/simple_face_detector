from webcamvideostream import WebcamVideoStream
 
class VideoStream:
        #default settings
	def __init__(self, src=0, usePiCamera=False, resolution=(720, 480),
		framerate=32):
		if usePiCamera:
			# only import this package if using PiCamera
			from pivideostream import PiVideoStream
 
			self.stream = PiVideoStream(resolution=resolution,
				framerate=framerate)
 
		# otherwise, we are using OpenCV so initialize the webcam
		# stream
		else:
			self.stream = WebcamVideoStream(src=src)
			
			
def start(self):
		# start the threaded video stream
		return self.stream.start()
 
	def update(self):
		# grab the next frame from the stream
		self.stream.update()
 
	def read(self):
		# return the current frame
		return self.stream.read()
 
	def stop(self):
		# stop the thread and release any resources
		self.stream.stop()