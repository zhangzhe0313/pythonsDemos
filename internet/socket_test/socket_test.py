#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: socket_test.py
# @Time: 2019-1-17 10:50

import socket, datetime

ip_port = ('127.0.0.1', 9999)

skt = socket.socket()
skt.bind(ip_port)
skt.listen(5)
conn, addr = skt.accept()
data = '服务已建立'
conn.send(data.encode())
while True:
    back = conn.recv(1024)
    if back == b'exit':
        break
    else:
        print(datetime.datetime.now(), back.decode())
conn.close()
skt.close()