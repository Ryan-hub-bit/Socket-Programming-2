#!/usr/bin/env python3
#UDPPingerClient.py
# Tony Yang, tyang27

from socket import *
import time

# Stats
stats = []
N = 10
N_timeout = 0

# Configuration
t_timeout = 1.0

# Destination
host = 'localhost'
port = 12000

for i in range(N):
  # DGRAM for UDP
  skt = socket(AF_INET, SOCK_DGRAM)
  skt.settimeout(t_timeout)

  # Message
  message = f'Ping {i+1} {time.ctime()}'.encode()

  start = time.time()
  skt.sendto(message, (host, port))
  try:
    result = skt.recv(10000).decode()
    end = time.time()

    print(f'{result} {end-start}')
    stats.append(end-start)

  except:
    print('Request timed out')
    N_timeout += 1

min_RTT = min(stats) if len(stats) > 0 else 'All requests timed out'
max_RTT = max(stats) if len(stats) > 0 else 'All requests timed out'
avg_RTT = sum(stats) / len(stats) if len(stats) > 0 else 'All requests timed out'
loss = (1 - len(stats) / N) * 100

print(f'min: {min_RTT}')
print(f'max: {max_RTT}')
print(f'avg: {avg_RTT}')
print(f'packet loss rate: {loss}%')
