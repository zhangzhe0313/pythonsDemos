# 客户端
import socket

# 创建实例
sk = socket.socket()
# 设置服务器ip和端口
ip_port = ('127.0.0.1', 8888)
# 连接服务器
sk.connect(ip_port)
while True:
    # 接受服务器连接信息
    connInfo = sk.recv(1024)
    print(connInfo.decode())
    data = input('请输入客户端信息：')
    if data == 'quit':
        break
    sk.send(data.encode())
    receiveData = sk.recv(1024)
    print(receiveData.decode())
# 关闭连接
sk.close()
