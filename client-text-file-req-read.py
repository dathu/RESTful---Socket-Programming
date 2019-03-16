#**********************CREATED BY AMULYA SURESH, RACHANA U POLE, EWT SOIS, MANIPAL*******************************************************************
import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60003                    # Reserve a port for your service.

s.connect((host, port))
my_input='HEllo server'
my_input = my_input.encode('utf-8')
s.sendall(my_input)


with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
