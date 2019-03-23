try:
 import socket
 import threading 
 import time
except:
	print("library not found")

HOST = '127.0.0.1'
PORT = 8018


def my_client():
	threading.Timer(11,my_client).start()
	with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
		s.connect((HOST,PORT))
		#inp='Hello'
		#inp=inp.encode('utf-16')
		#s.sendall(inp)
		inp = int(input("enter the values"))
		inp = inp.encode('utf-16')
		s.sendall(inp)
		data=s.recv(1024).decode('utf-16')

		print("average is  ", data)
		s.close()

if __name__ == '__main__':
	#while 1 :
	my_client()
