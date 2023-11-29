import socket
'''
grabsock = socket.socket()
ip = input ('IP Here: ')
port = str(input('Port Here: '))
grabsock.connect((ip, int(port)))

print(grabsock.recv(1024))'''

def banner(ip, port):
    sockgrab = socket.socket()
    sockgrab.connect((ip, int(port)))
    sockgrab.settimeout(3)
    print(sockgrab.recv(1024))


def main():
    ip = input('IP Here: ')
    port = input('Port Here: ')
    banner(ip, port)

main()