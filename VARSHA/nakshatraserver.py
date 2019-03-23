import socket
import encodings

HOST = '127.0.0.1'
PORT = 8018

def avg():
 	sum = int+2*int
 	average = str(sum/2)
 	return average

def my_server():
	with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
 		print("server waiting for the client to connect")
 		s.bind((HOST,PORT))
 		s.listen(5)
 		conn,addr = s.accept()

 		with conn:
 			print("Connected by ",addr)
 			while True:
 				data = conn.recv(1024).decode('utf-16')
 				if str(data)==int :
 					print("ok sending the data")
 				
 					x_encoded_data = avg().encode('utf-16')
 					conn.sendall(x_encoded_data)
 				elif str(data) =="QUIT":
 					print("shutting down")
 					break
 				if not data:
 					break
 				else:
 					pass
if __name__ == '__main__':
#	while 1:
	my_server()
 	