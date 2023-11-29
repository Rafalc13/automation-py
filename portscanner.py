import socket

sockport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockport.settimeout(3)

host = input('IP Here: ')
port = int(input('Port Here: '))

def portScanner(port):
    if sockport.connect_ex((host, port)):
        print('closed port reach')
    else:
        print('port is welcoming')
portScanner(port)