
#*******THIS SCRIPT IS CODED BY VARSHINI L AND YUVARAJ G FROM EWT ,SOIS,MAHE,MANIPAL************
#THIS SCRIPT OUTPUTS THE CURRENT DATE AND TIME ,CALENDAR OF MONTH AND YEAR SPECIFIED,IP ADDRESS OF THE SERVER 
import socket
from datetime import datetime
import encodings
import calendar
HOST='127.0.0.1'
PORT=65430
def get_time():
    tim=str(datetime.now())
    return tim
def get_cal():
    yy = 2019
    mm = 2
    return calendar.month(yy, mm)
def get_IP():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return str(IPAddr)

def my_server():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        print("Server Started......")
        s.bind((HOST,PORT))
        s.listen(5)
        conn,addr=s.accept()
        with conn:
            print("connected bt",addr)
            while True:
                data=conn.recv(1024).decode('utf-16')
                if str(data)=='Hello':
                    current_time=get_time()
                    output=current_time.encode('utf-16')
                    conn.sendall(output)
                    calendar=get_cal().encode('utf-16')
                    conn.sendall(calendar)
                    Ip=get_IP()
                    conn.sendall(Ip)

                    
                elif str(data) == "Quit":
                    print("Shutting Down....")
                    
                if not data:
                    break
                else:
                    pass
            

if __name__=='__main__':
    while 1:
        my_server()
    