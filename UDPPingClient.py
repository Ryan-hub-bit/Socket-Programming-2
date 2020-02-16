import time
from socket import *

# ping from 1-10

for pings in range(10):
    # Create a UDP socket Sock_DGRAM
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    # timeout option allows the user to select the amount of time(in seconds) to wait between successive attempts to
    # connect to the printer.
    clientSocket.settimeout(1.0)
    # ping to server
    message = f'Ping'.encode()

    address = ('Localhost', 12000)
    # Send ping
    start = time.time()
    clientSocket.sendto(message, address)

    # if data is received back from server, print
    try:
        data = clientSocket.recv(1024).decode()
        end = time.time()
        timeDifference = end - start
        print(f'{data}{pings}{timeDifference}')
    except timeout:
        print('REQUEST TIMED OUT')

