import re

RE = "[0-9]{5}_[0-9]{6}_(f|h|r|q)[a-z](.){5}bz2" #exemplo de regex

lexical_analiser = re.compile(RE) #compila a expressao regular

lexical_analiser.search("Palavra a ser buscada") #busca o regex na palavra desejada
