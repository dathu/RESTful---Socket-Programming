Megahana.M.C
181040005, EWT, Sois

We are implementing Client-Server date-time, calendar and host_name socket programming 
*We are taking the request to display the current date-time, host name and calendar to the client and passing the corresponding request to the client.
*After receiving the request all the data which is requested are displayed on the client.                                                                                                                                                       conn,addr=s.accept()

        with conn:
            print("connected by",addr)
            while True:
                data=conn.recv(1024).decode('utf-16')
                if str(data)=='Hello':
                    current_time=get_time().encode('utf-16')
                    conn.sendall(current_time)

                    host_name=get_host_name().encode('utf-16')
                    conn.sendall(host_name)
                 
                    calendar=get_cal().encode('utf-16')
                    conn.sendall(calendar)
                   
                elif str(data) == "Quit":
                    print("Shutting Down....")
                    
                if not data:
                    break
                else:
                    pass
            

if __name__=='__main__':
    #while 1:
    my_server()
    