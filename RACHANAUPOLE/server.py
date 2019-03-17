#**************************RACHANA U POLE,EWT,SOIS,MANIPAL**************************
import socket
HOST='127.0.0.1'
PORT=65430
s=socket.socket()
s.bind((HOST,PORT))
s.listen(5)
while True:
    conn,addr=s.accept()
    data=conn.recv(1024).decode('utf-8')
    if str(data)=='first':
        print(data)
        filename='first.txt'
        f=open(filename,'rb')
        l=f.read(1024)
        while(l):
            conn.sendall(l)
            l=f.read(1024)
    elif str(data)=='second':
        print(data)
        filename='second.txt'
        f=open(filename,'rb')
        l=f.read(1024)
        while(l):
            conn.sendall(l)
            l=f.read(1024)
    elif str(data)=='third.txt':
        print(data)
        filename='third.txt'
        f=open(filename,'rb')
        l=f.read(1024)
        while(l):
            conn.sendall(l)
            l=f.read(1024)
    elif str(data)=="quit":
        print("shutting down server ")
        break
    else:
        pass
    f.close()
conn.close()
