# 服务器
import socket
import random

# 创建实例
sk = socket.socket()
# 设置服务器ip和端口
ip_port = ('127.0.0.1', 8888)
# 绑定端口ip
sk.bind(ip_port)
# 设置最大连接数
sk.listen(5)
# 服务器连接成功后信息
connInfo = '客户端成功连接'
while True:
    # 监听连接
    conn, adress = sk.accept()
    # 发送连接成功信息
    conn.send(connInfo.encode())
    while True:
        data = conn.recv(1024)
        if data == b'quit':
            break
        print(data.decode())
        conn.send(data)
        conn.send(str(random.randint(1, 1000)).encode())
    conn.close()
