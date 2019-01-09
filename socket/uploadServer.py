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
        with open('testFile.txt', 'ab') as f:
            data = conn.recv(1024)
            f.write(data)
        f.close()
        conn.send('success'.encode())
    conn.close()
sk.close()
