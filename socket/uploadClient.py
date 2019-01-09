#!usr/bin/env pathon
# -*- coding: UTF-8 -*-


# 上传文件
import socket

# 实例化
sk = socket.socket()
# 设置ip和端口
ip_port = ('127.0.0.1', 8888)
# 连接服务器
sk.connect(ip_port)
data = sk.recv(1024)
print(data.decode())
try:
    f = open('tcpClient.py', 'rb')
except IOError as err:
    print(err)
else:
    for i in f:
        sk.send(i)
        data = sk.recv(1024)
        if data != b'success':
            break
finally:
    f.close()
sk.close()
