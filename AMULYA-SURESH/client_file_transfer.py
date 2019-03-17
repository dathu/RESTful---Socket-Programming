import socket
HOST='127.0.0.1'
PORT=65434
s=socket.socket()
s.connect((HOST,PORT))
with open('recieved.txt','wb') as f:
    data=s.recv(1024)
    f.write(data)
    print("data is copying")
f.close()
s.close()

