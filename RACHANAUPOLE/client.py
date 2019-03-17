#*****************************RACHANA U POLE,EWT,SOIS,MANIPAL**************************
import socket
import time
HOST='127.0.0.1'
PORT=65430
def myclient():
    s=socket.socket()
    s.connect((HOST,PORT))
    myinput=input('Enter the file you want to Fetch')
    encod_my=myinput.encode('utf-8')
    s.sendall(encod_my)
    with open('received.txt','ab') as f:
        data=s.recv(1024)
        f.write(data)
    print('sending successful')
    time.sleep(5)
    f.close()

if __name__=='__main__':
    while 1:
        myclient()

