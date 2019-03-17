try:
    import socket
    import threading
    import time
except:
    print("No Library Found ")
    
HOST=socket.gethostname()
PORT=65441

def my_client():
    threading.Timer(30,my_client).start()
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        inp='Hello'
        inp=inp.encode('utf-16')
        s.sendall(inp)
        data=s.recv(1024).decode('utf-16')
        data1=s.recv(1024).decode('utf-16')
        data2=s.recv(1024).decode('utf-16')

        print("current time is",data)
        print("Host name is:", data1)
        print("calander : ", data2)
 
        s.close()
     #   time.sleep(5)

if __name__=='__main__':
    #while 1:
    my_client()
    