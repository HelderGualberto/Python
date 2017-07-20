# This script allow to copy files with the same name as the directory, using regex expression

import re, os, subprocess, sys

source = sys.argv[1]
destiny = sys.argv[2]

print "Source folder: " + source
print "Destiny folder: " + destiny

def search(string,folder):
	for f in folder:
		if string.find(f) >= 0:
			return f
	
	return None


def moveImg(img_from,img_to):	
	subprocess.call(["mv",img_from,img_to])


sub_des = os.listdir(destiny)
files = os.listdir(source)



for f in files:
	img_from = source + "/" + f.strip()

	img_to = search(f,sub_des)
	if not img_to is None:
		img_to = destiny + img_to +"/"+f.strip()
		print "From: " + img_from
		print "To: " + img_to
		#moveImg(img_from,img_to)
	else
		print "Regex not found"
		