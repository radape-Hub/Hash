"""
este script realiza la conversión de cualquier cadena de texto a las funciones hash en las cuatro
formas de caracteres hexadecimales. 

"""


import hashlib
import argparse
import logging
from colorama import init, Fore, Back, Style


init(autoreset= True)

entradaTex = argparse.ArgumentParser( prog="Generador Hash", usage= '%(prog)s', description= "Genera Hash para el texto que se digita", epilog = "Este script realiza la conversión de un texto en un algoritmo hash")
entradaTex.add_argument("-t", dest= "texto", help = "Indica el texto de entrada sin espacios o entre comillas", required = True )
entradaTex.add_argument("-g", dest= "guardar", help = "Responder de forma afirmativa para guardar la información en un archivo o de forma negativa para no guardar", required= True )

datoentra = entradaTex.parse_args()

tex = datoentra.texto
gua = datoentra.guardar



def calcuHash(datoen):
	datobi = datoen.encode()
	hasmd5 = hashlib.md5(datobi)
	hassha1 = hashlib.sha1 (datobi)
	hassha224= hashlib.sha224(datobi)
	hassha256= hashlib.sha256(datobi)
	return (("hash md5 del texto que se ingresó: {} --> ".format(Back.CYAN+datoen+Back.RESET),Fore.GREEN+Style.BRIGHT+hasmd5.hexdigest()),
	("hash sha1 del texto que se ingresó: {} --> ".format(Back.CYAN+datoen+Back.RESET),Fore.GREEN+Style.BRIGHT+hassha1.hexdigest()),
	("hash sha224 del texto que se ingresó: {} --> ".format(Back.CYAN+datoen+Back.RESET),Fore.GREEN+Style.BRIGHT+ hassha224.hexdigest()),
	("hash sha256 del texto que se ingresó: {} --> ".format(Back.CYAN+datoen+Back.RESET),Fore.GREEN+Style.BRIGHT+ hassha256.hexdigest()))

archi = calcuHash (tex)

for a, b in archi:
	print('\n'+ a +  b )

if gua in ('s', 'si', 'S', 'SI', 'Si', 'yes', 'YES'):

	with open ("recoHash.txt", "a+") as f:
		for i, j in archi:
			f.write('\n'+ i +  j +'\n')
			
	print (Fore.RED+Style.BRIGHT+"\nLa información se guardo en archivo llamado recoHash.txt \n")
			

else:
	print (Fore.RED+Style.BRIGHT+"\nLa información no se guardo ")







