try:
	import socket
	import threading
	import time
except:
	print('library not found')

HOST = '127.0.0.1'
PORT = 65432

def my_client():
	
	threading.Timer(11, my_client).start()
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))

		my_inp = 'Data'
		my_inp = my_inp.encode('utf-8')
		s.sendall(my_inp)

		data  = s.recv(1024).decode('ascii')

		print(data)
		
		s.close()
		time.sleep(5)

if __name__ == "__main__":
	while 1:
		my_client()
