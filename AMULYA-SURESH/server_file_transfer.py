#***the server mainly comprises of creation of SOCKET,BIND,LISTEN,ACCEPT***
import socket
HOST='127.0.0.1'
PORT=65434
s=socket.socket()          #*socket object is created 
s.bind((HOST,PORT))             
s.listen(5)
while True:
    conn,addr=s.accept()
    filename='mytext.txt'      #* create a file which is to be transferred
    f=open(filename,'rb')      #read the filename in readbinery format
    l=f.read(1024)             # sent per max of 1024 bytes of data
    while(l):
        conn.sendall(l)         
        l=f.read(1024)
        f.close()
    conn.close()
    
