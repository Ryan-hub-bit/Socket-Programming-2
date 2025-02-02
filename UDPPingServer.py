import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packet
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
print('waiting for receiving data')

while True:
    # Generate random number in the rande of 0 to 10
    rand = random.randint(0, 10)
    # Receive client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    # Capitalize the message from the client
    message = message.upper()
    # if rand is less than 4, consider the packet lost do not respond
    if rand < 4:
        continue
    # Otherwise, the server responds
    serverSocket.sendto(message, address)

