# -*- coding:utf-8 -*-
from socket import *

HOST = ''
PORT = 50000
ADDR = (HOST, PORT)
BUFF_SIZE = 1024

print("Waiting Server...")
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(ADDR)
serverSocket.listen(5)

clientSocket, addr = serverSocket.accept()
print("*** Connected ***")

while True:
    try:
        clientData = clientSocket.recv(BUFF_SIZE)
        print("client msg : ", clientData.decode())

        serverData = clientSocket.send(clientData)

        print("-=" * 20)

    except Exception as e:
        clientSocket.close()
