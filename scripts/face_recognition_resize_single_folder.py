import cv2, subprocess, os, multiprocessing, sys

def resize_img(faces_rect,img_cv):
	x = faces_rect[0]
	y = faces_rect[1]
	w = faces_rect[2]
	h = faces_rect[3]

	im_height = img_cv.shape[0] # shape index 0 shows the image height value
	im_width = img_cv.shape[1] # shape index 0 shows the image width value

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

cascade_path = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"
root_path = sys.argv[1]

files = os.listdir(root_path)
facecascade = cv2.CascadeClassifier(cascade_path)
MAX_OF_THREADS = 9

def detect_faces(img_path,img_name):

	print img_path
	# open the img file 
		
	try:
		img_cv = cv2.imread(img_path,cv2.CV_LOAD_IMAGE_COLOR)
		img_gray = cv2.cvtColor(img_cv,cv2.COLOR_BGR2GRAY)
	except:
		try:
			img_cv = cv2.imread(img_path,cv2.CV_LOAD_IMAGE_GRAYSCALE)
			img_gray = i.mg_cv

		except Exception:
			print "Error converting image"
			log_file = open("../log_files/face_detect_log.txt","a")
			log_file.write("Error converting image: " + img_path + "\n")
			log_file.close()
			return

	# call the cascade classifier where you select what kind of cascade will you use
	#Convert the input image to an gray scaled image
	
	faces = []
	#passog = 1.05
	#scale = 1.001
	#while scale < 1.20:
	try:
		#detectMultiscale is an general function to recognize objects, depends on the selected cascade
		faces = facecascade.detectMultiScale(
			img_gray, #grays caled image
			scaleFactor=1.1, # scale of the image
			minNeighbors=5, #number of faces detected in a range
			minSize=(90,90), #min size of an image
			flags=cv2.cv.CV_HAAR_SCALE_IMAGE
		)
	except Exception:
		print "Error trying to detect faces"
#		scale *= passog 
#		if len(faces)!=0:
#			break 

	if len(faces)!=0:
		face_rect = faces[0]
		img_cv = resize_img(face_rect,img_cv)
		# to get the tuple in a array we only need to use a simple variable
		# to get the tuple elements we need to use the variable with parentheses like (a)
		cv2.imwrite(img_path,img_cv)

	else:
		log_file = open("../log_files/face_detect_log.txt","a")
		log_file.write("No faces found in: " + img_path + "\n")
		log_file.close()
		subprocess.call(["mv",img_path,"/srv/not_crop/"+img_name])
def main():

	for img in files:
		if __name__ == '__main__':
			while len(multiprocessing.active_children()) > MAX_OF_THREADS:
				pass
			img_path = root_path + "/" + img.strip()
			p = multiprocessing.Process(target=detect_faces,args=(img_path,img.strip(),)
			p.start()
		

main()
log_file.close()