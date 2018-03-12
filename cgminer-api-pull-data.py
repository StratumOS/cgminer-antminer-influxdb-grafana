#!/usr/bin/env python3
# Usage:
# cgminer-api-pull-data.py [command] [ip] [port]
# eg. cgminer-api-pull-data.py summary 192.168.1.10 4028
#

import socket
import json
import sys


def linesplit(socket):
    buffer = socket.recv(4096).decode()
    done = False
    while not done:
        more = socket.recv(4096).decode()
        if not more:
            done = True
        else:
            bufferdecode = buffer + more
    if buffer:
        return buffer

api_command = sys.argv[1].split('|')

if len(sys.argv) < 3:
    api_ip = '127.0.0.1'
    api_port = 4028
else:
    api_ip = sys.argv[2]
    api_port = sys.argv[3]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((api_ip, int(api_port)))
if len(api_command) == 2:
    s.send(json.dumps({"command": api_command[0], "parameter": api_command[1]}))
else:
    resp = s.send(json.dumps({"command": api_command[0]}).encode())

#print(resp)
response = linesplit(s)
response = response.replace('\x00', '')
response = json.loads(response)
print(response)
s.close()
