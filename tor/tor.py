import socks
import requests
import socket
import json

def main():
	print('Peticion sin tor: ' + requests.get('https://ifconfig.me').text)

	socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9050)

	socket.socket = socks.socksocket

	print('Peticion con TOR: ' + requests.get('https://ifconfig.me').text)

if __name__ == '__main__':
	main()
