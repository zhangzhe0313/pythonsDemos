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
# 捕获异常
try:
    # with 执行完，自动关闭文件
    with open('tcpClient.py', 'rb') as f:
        # 未出错，发送准备就绪消息
        msg = 'onReady'
        sk.send(msg.encode())
        # 接受服务器返回的确认信息
        svBack = sk.recv(1024)
        # 服务器确认就绪
        if svBack == b'ACK':
            print('服务器已准备就绪: %s' % (svBack.decode()))
            for i in f:
                sk.send(i)
                if sk.recv(1024) == b'recieve over':
                    print('recieve over')
                    continue
            # 关闭连接
            finish = 'finish'
            sk.send(finish.encode())
            sk.close()
            print('客户端已上传完成')
        # 服务器未确认就绪
        else:
            print('服务器未准备就绪：%s' % (svBack))
            sk.close()
except Exception as err:
    print('客户端文件准备失败：%s' % (err))
    msg = 'onFail'
    sk.send(msg.encode())
    sk.close()
