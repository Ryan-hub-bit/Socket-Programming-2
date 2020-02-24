#!/usr/bin/env python3
#UDPPingerClient.py
# Tony Yang, tyang27

from socket import *
import sys
import time

# Stats
stats = []
N = 10
N_timeout = 0

# Configuration
t_timeout = 1.0

# Destination
#host = 'localhost'
#port = 12000
host = sys.argv[1]
port = int(sys.argv[2])

for i in range(N):
  # DGRAM for UDP
  skt = socket(AF_INET, SOCK_DGRAM)
  skt.settimeout(t_timeout)

  # Message
  t = time.strftime('%H:%M:%S', time.localtime())
  message = f'Ping {i+1} {t}'.encode()

  start = time.time()
  skt.sendto(message, (host, port))
  try:
    result = skt.recv(10000).decode()
    end = time.time()

    print(f'{result} RTT = {end-start}s')
    stats.append(end-start)

  except:
    print('Request timed out')
    N_timeout += 1

min_RTT = min(stats) if len(stats) > 0 else 'All requests timed out'
max_RTT = max(stats) if len(stats) > 0 else 'All requests timed out'
avg_RTT = sum(stats) / len(stats) if len(stats) > 0 else 'All requests timed out'
loss = (N_timeout / N) * 100

print(f'Max ping time was {max_RTT}s')
print(f'Min ping time was {min_RTT}s')
print(f'Avg ping time was  {avg_RTT}s')
print(f'Package loss rate was {int(loss)}%')
