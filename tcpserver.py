import socket

servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = 127.0.0.1
host = socket.gethostname()
port = 444

servsock.bind((host, port))
servsock.listen(13)

while True:
    clientsocket, address = servsock.accept()
    print('connection appears from %s' % str(address))
    message = 'Hey Little Wolf! Welcome to the pack' + "\r\n"
    
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()