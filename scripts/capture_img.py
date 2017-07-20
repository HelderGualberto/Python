import cv2, copy
capture = cv2.VideoCapture("/home/user/extra/safety_city/teste/video1.mp4") 
img_tuple = []
CV_CAP_PROP_FRAME_WIDTH = 3
CV_CAP_PROP_FRAME_HEIGHT = 4
CV_CAP_PROP_FPS = 5

capture.set(CV_CAP_PROP_FRAME_WIDTH,500)
capture.set(CV_CAP_PROP_FRAME_HEIGHT,500)
capture.set(CV_CAP_PROP_FPS,30)

while True:
	if(capture.isOpened()):
		img_tuple = capture.read()

		if(img_tuple[0] == 1):
			sImg = []
			img = copy.copy(img_tuple[1])
			cv2.resize(img,sImg, (500,500),fx=0, fy=0, interpolation=1 )
			
			rows,cols,color = img_tuple[1].shape
			rot = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
			cv2.warpAffine(img,rot,(cols,rows))

			cv2.imshow("teste",img)
			cv2.waitKey(20) #30fps
	else:
		print "Impossible to open the camera or video" 
		break