import os
import socks
import requests
import socket
import json
import threading
import string
import base64
import urllib.request
import urllib.parse
import time
import sys
import random



#Conexión a RED TOR
os.system("clear")
print ("Conectando a la red TOR! ")
os.system("sudo service tor start")


def main():
	#Comprobar conexiones
	print ('Comprobando conexion a TOR! ')
	print ('\tConexion sin TOR: ' + requests.get('https://ifconfig.me').text)

	socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9050)

	socket.socket = socks.socksocket

	p = requests.get('https://ifconfig.me')
	data1 = requests.get('https://ipinfo.io/{}'.format(p.text))

	data = json.loads(data1.text)

	print ('\tConexion con TOR: ' + p.text)
	print ("\t\tPais: {}".format(data['country']))
	print ("\t\tRegion: {}".format(data['region']))
	print ("\t\tCiudad: {}".format(data['city']))
	print ("\t\tHostname: {}".format(data['hostname']))
	print ("\t\tPostal: {}".format(data['postal']))

	print ('\n\n   ESTAS CONECTADO A TOR!')

	#Comienzo del SMS
	print ('Por favor introduce los detalles del SMS')
	cc = input("\t   Pon el Codigo del PAIS (SIN EL +) (Ejemplo: Chile = '56')")
	pn = input("\t   Pon el Numero del Telefono : +" + cc + " ")
	numbe = cc + pn
	receiver = '+' + numbe
	text = input("\t   Introduce el mensaje que quieres enviar! : \n\t\t   >>>")
	resp = requests.post('https://textbelt.com/text',{
		'phone' : receiver,
		'message' : text ,
		'key' : 'textbelt'
	})

	print (resp.json())
	print ("Listo")

if __name__ == '__main__':
	main()
