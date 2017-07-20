
#Aplica o filtro para eliminar as imagens repetidas e as imagens intrusas nos individuos

import os, subprocess, sys

arq_filter = sys.argv[3] # local do arquivo com os filtros

filter_file = open(arq_filter)

f = filter_file.read()

data_root_path = sys.argv[1] #pasta da fonte dos dados
destiny_folder = sys.argv[2] #pasta de destino dos dados]

f = f.split('\r\n')

for data in f:
	line = data.split(',')
	
	try:
		img = data_root_path +"/"+ line[1] +"/"+line[0]
		img_destiny = destiny_folder + "/" + line[0]
		subprocess.call(["mv",img,img_destiny])
	except Exception:
		print img + "nao encontrada"
		pass