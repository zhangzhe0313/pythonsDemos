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
# 循环
while True:
    msg = '服务器已连接'
    conn, adress = sk.accept()
    conn.send(msg.encode())
    while True:
        # 捕获异常
        try:
            f = open('testFile.txt', 'ab')
        # 捕获异常类型：如果不加类型则会捕获所有类型，若使用Exception 则会捕获除了与程序退出相关的其他异常
        except IOError as err:
            print('文件打开失败：%s' % (err))
        # 若是try中执行未出错，则执行else
        else:
            data = conn.recv(1024)
            f.write(data)
        # 最终都会执行
        finally:
            f.close()
        conn.send('success'.encode())
    conn.close()
sk.close()
