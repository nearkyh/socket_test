# -*- coding:utf-8 -*-
from socket import *

HOST = ''
PORT = 50000
ADDR = (HOST, PORT)
BUFF_SIZE = 1024

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(ADDR)

while True:
    try:
        msg = input("client msg>")
        clientData = clientSocket.send(msg.encode())

        serverData = clientSocket.recv(BUFF_SIZE)
        print("server msg>", serverData.decode())

        print("-=" * 20)

    except KeyboardInterrupt:
        clientSocket.close()
        sys.exit()
