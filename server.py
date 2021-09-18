import socket

# instantiate socket object
s = socket.socket()
print('Socket successfully created')
host = socket.gethostname()
port = 1420
s.bind((host, port))
print('socket binded to %s' %(port))

s.listen(5)
print('socket is listening. . .')
while True:
    # establish connection with client
    c, addr = s.accept()
    print ('Got connection from ', addr)
    c.send('Thank you for connecting'.encode)
    c.close()
    break