
#Rodar este script na pasta anterior a dos arquivos
import os

prefix = "./files/"
files = os.listdir(prefix)

for name in files:
    new_name = ''.join(e for e in name if e.isalnum())
    os.rename(prefix+name, prefix+new_name+'.pdf')



