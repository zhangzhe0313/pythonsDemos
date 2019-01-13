#!usr/bin/env pathon
# -*- coding: UTF-8 -*-


# 接受文件服务器
import socket

# 实例化
sk = socket.socket()
# 设置ip和端口
ip_port = ('127.0.0.1', 8888)
# 绑定ip和端口
sk.bind(ip_port)
# 设置最大连接数
sk.listen(5)
#
msg = '服务器已连接'
conn, adress = sk.accept()
conn.send(msg.encode())
# 接受到客户端准备就绪信号
info = conn.recv(1024)
if info == b'onReady':
    print('客户端准备就绪: %s ' % (info.decode()))
    try:
        with open('testFile.txt', 'ab') as f:
            # 成功打开文件，发送确认消息
            sure = 'ACK'
            conn.send(sure.encode())
            # 开始接受客户端发送文件信息
            while True:
                data = conn.recv(1024)
                if data == b'finish':
                    break
                else:
                    f.write(data)
                    conn.send('recieve over'.encode())
                    print('服务器 recieve over')
        conn.close()
        print('服务器接收完成')
    # 捕获异常类型：如果不加类型则会捕获所有类型，若使用Exception 则会捕获除了与程序退出相关的其他异常
    except Exception as err:
        print('服务器文件打开失败：%s' % (err))
        sure = 'onFail'
        conn.send(sure.encode())
        conn.close()
else:
    print('客户端准备失败: %s ' % (info.decode()))
    conn.close()
sk.close()