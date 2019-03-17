import socket
import numpy as np
import encodings
import time
import calendar
HOST = '127.0.0.1'
PORT = 65432      


def send_time():
    currentTime = time.ctime(time.time())+ "\r\n"
    return  currentTime

def cal():
    yy = 2019
    mm = 3
    return calendar.month(yy,mm)

    
    
    


def my_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Server Started waiting for client to connect ")
        s.bind((HOST
                , PORT))
        s.listen(5)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024).decode('utf-8')
                if str(data) == "Data":
                    print("Ok Sending data ")
                    ctime = send_time()
                    conn.send(ctime.encode('ascii'))
                    calender = cal()
                    conn.send(calender.encode('ascii'))
                    hostname=socket.gethostname()
                    ip = socket.gethostbyname(hostname)
                    conn.send(ip.encode('ascii'))
    
                elif str(data) == "Quit":
                    print("shutting down server ")
                    break
                if not data:
                    break
                else:
                    pass
if __name__ == '__main__':
    while 1:
        my_server()
