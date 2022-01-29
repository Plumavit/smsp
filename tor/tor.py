import socks
import requests
import socket
import json

def main():
	print ('Petición sin TOR: ' + requests.get('https://ifconfig.me').text)

	socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9050)

	socket.socket = socks.socksocket

	p = requests.get('https://ifconfig.me')
	data1 = requests.get('https://ipinfo.io/{}'.format(p.text))

	data = json.loads(data1.text)

	print ('Petición con TOR: ' + p.text)
	print ("\tPais: {}".format(data['country']))
	print ("\tRegion: {}".format(data['region']))
	print ("\tCiudad: {}".format(data['city']))
	print ("\tHostname: {}".format(data['hostname']))
	print ("\tPostal: {}".format(data['postal']))


if __name__ == '__main__':
	main()
