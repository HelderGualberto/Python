# Algoritmo para colocar as imagens do mesmo individuo em uma unica pasta. 
# Serao buscandas imagens em pasta com o regex 'nome_sobrenome' e colocadas em 'nome sobrenome'
 
import re, os, subprocess

root_path = "/home/user/extra/data/raw"

def moveImg(img_from,img_to):
	copy_files_path = root_path +"/"+img_from

	files = os.listdir(copy_files_path)

	for f in files:
		origin_img = copy_files_path + "/" + f
		destiny_img = root_path + "/" + img_to + "/" + f
		
		subprocess.call(["mv",origin_img,destiny_img])


folders = os.listdir(root_path)

regex = re.compile("_")

underline = []
nounderline = []
i=0
j=0
for f in folders:
	if(regex.search(f)):
		underline.insert(i,f)
		i+=1
	else:
		nounderline.insert(j,f)
		j+=1

for under in underline:
	tmp = under.replace("_"," ")
	for nounder in nounderline:
		if nounder == tmp:
			moveImg(under,nounder)
