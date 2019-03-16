
#*****This script is wriiten by Varshini L and Yuvaraj G from SOIS,MAHE,Maniapl*******************
#THIS SCRIPT OUTPUTS THE CURRENT DATE AND TIME ,CALENDAR OF MONTH AND YEAR SPECIFIED,IP ADDRESS OF THE SEVER 
try:
    import socket
    import threading
    import time
except:
    print("No Library Found ")
    
HOST='127.0.0.1'
PORT=65430
def my_client():
    threading.Timer(11,my_client).start()
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        inp='Hello'
        inp=inp.encode('utf-16')
        s.sendall(inp)
        data=s.recv(1024).decode('utf-16')
        data1=s.recv(1024).decode('utf-16')
        data2=s.recv(1024).decode('utf-16')
        print("current time is",data)
        print("calendar of",data1)
        print("IP ADDRESS is",data2)

    
        s.close()
        #time.sleep(5)
if __name__=='__main__':
    #while 1:
    my_client()
    