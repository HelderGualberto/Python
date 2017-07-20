import cv2, subprocess, os, multiprocessing, sys

def resize_img(faces_rect,img_cv):
	x = faces_rect[0]
	y = faces_rect[1]
	w = faces_rect[2]
	h = faces_rect[3]

	im_height = img_cv.shape[0] # shape index 0 shows the image height value
	im_width = img_cv.shape[1] # shape index 0 shows the image height value

	if x > w/4: #that means the resultant X value is smaller than the old x
		faces_rect[0] = x - (w/8)
	else:
		faces_rect[0] = 0

	if y > h/4: #that means the resultant Y value is smaller than the old y
		faces_rect[1] = y - (h/8)
	else:
		faces_rect[1] = 0

	if im_height > h*5/4:
		faces_rect[2] = h*5/4
	else:
		faces_rect[2] = im_height

	if im_width > w*5/4:
		faces_rect[3] = w*5/4
	else:
		faces_rect[3] = im_width

	x = faces_rect[0]
	y = faces_rect[1]
	w = faces_rect[2]
	h = faces_rect[3]

	crop_img = img_cv[y:y+h,x:x+w]

	return crop_img	

# select the path of the haarcascade.xlm file 

cascade_path = "/home/user/opencv-2.4.12/data/haarcascades/haarcascade_eye.xml"
root_path = sys.argv[1]
sub_folders = os.listdir(root_path)
facecascade = cv2.CascadeClassifier(cascade_path)
log_file = open("../log_files/eye_detect_log.txt","wr")
MAX_OF_THREADS = 1

def detect_eyes(i,j,img_files):

	img_name_path = root_path+"/"+sub_folders[i]+"/"+img_files[j]
	print img_name_path
	# open the img file 
		
	try:
		img_cv = cv2.imread(img_name_path,cv2.CV_LOAD_IMAGE_COLOR)
		img_gray = cv2.cvtColor(img_cv,cv2.COLOR_BGR2GRAY)
	except:
		try:
			img_cv = cv2.imread(img_name_path,cv2.CV_LOAD_IMAGE_GRAYSCALE)
			img_gray = i.mg_cv

		except Exception:
			print "Error converting image"
			return

	# call the cascade classifier where you select what kind of cascade will you use
	#Convert the input image to an gray scaled image
	
	eyes = []


	try:
		#detectMultiscale is an general function to recognize objects, depends on the selected cascade
		eyes = facecascade.detectMultiScale(
			img_gray, #gray scaled image
			scaleFactor=1.1, # scale of the image
			minNeighbors=5, #number of faces detected in a range
			minSize=(30,30), #min size of an image
			flags=cv2.cv.CV_HAAR_SCALE_IMAGE
		)
	except Exception:
		print "Error trying to detect eyes"
	x=0
	while x < len(eyes):
		
		p1 = (eyes[x][0],eyes[x][1])
		p2 = (eyes[x][0] + eyes[x][2],eyes[x][1] + eyes[x][3])
		cv2.rectangle(img_cv,p1,p2,(255,255,0),1)
		cv2.line(img_cv,p1,p2,(255,255,0),1)
		p1 = (p1[0] + eyes[x][2],p1[1])
		p2 = (p2[0] - eyes[x][2],p2[1])

		cv2.line(img_cv,p1,p2,(255,255,0),1)
		
		# to get the tuple in a array we only need to use a simple variable
		# to get the tuple elements we need to use the variable with parentheses like (a)
		#cv2.imwrite(img_name_path,img_cv)
		x+=1
	
	cv2.imshow("teste",img_cv)
	cv2.waitKey(0)

	#else:
	#	log_file.write("No eyes found in: " + img_name_path)
	#	subprocess.call(["rm",img_name_path])

def main():
	for i in range(0,len(sub_folders)):
		img_files = os.listdir(root_path +"/"+sub_folders[i])
		for j in range(len(img_files)):
			while len(multiprocessing.active_children()) > MAX_OF_THREADS:
				pass

			p = multiprocessing.Process(target=detect_eyes,args=(i,j,img_files,))
			p.start()
		

main()
log_file.close()