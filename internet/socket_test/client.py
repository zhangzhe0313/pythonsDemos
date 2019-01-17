#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: client.py
# @Time: 2019-1-17 10:55

import socket

ip_port = ('127.0.0.1', 9999)

skt = socket.create_connection(ip_port)

data = skt.recv(1024)
print(data.decode())
while True:
    sendData = input('请输入：')
    skt.send(sendData.encode())
    if sendData == 'exit':
        break
skt.close()

