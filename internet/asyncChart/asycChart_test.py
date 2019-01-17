#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: asycChart_test.py
# @Time: 2019-1-17 9:21

# 使用asyncchat的异步http服务器
import asynchat, asyncore, socket
import os
import mimetypes

try:
    # python3
    from http.client import responses
except ImportError:
    #python2
    from httplib import responses

# 该类继承自asyncore模块，仅处理接受的模块
class async_http(asyncore.dispatcher):
    def __init__(self, ip_port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(ip_port)
        self.listen(5)
        print('async_http __init__')

    def handle_accept(self):
        client, addr = self.accept()
        print('async_http handle_accept')
        return async_http_handler(client)


# 处理异步http请求的类
class async_http_handler(asynchat.async_chat):
    def __init__(self, conn = None):
        asynchat.async_chat.__init__(self, conn)
        self.datas = []
        self.got_header = False
        self.set_terminator(b'\r\n\r\n')

    # 获取传入数据并添加到缓存区
    def collect_incoming_data(self, data):
        if not self.got_header:
            self.datas.append(data)

    # 到达终止符，空白行
    def found_terminator(self):
        self.got_header = True
        header_data = b"".join(self.datas)
        # 将报头数据（二进制）解码成文本以便进一步处理
        header_text = header_data.decode('latin-1')
        header_lines = header_text.splitlines()
        request = header_lines[0].split()
        op = request[0]
        url = request[1][1:]
        self.process_request(op, url)

    # 将文本加入到传出流，但是首先要进过编码
    def push_text(self, text):
        self.push(text.encode('latin-1'))

    # 处理请求
    def process_request(self, op, url):
        if op == 'GET':
            if not os.path.exists(url):
                self.send_error(404, 'File %s not found!\r\n')
            else:
                type, encoding = mimetypes.guess_type(url)
                size = os.path.getsize(url)

                self.push_text('http/1.0 200 OK\r\n')
                self.push_text('Content-length: %s\r\n' % size)
                self.push_text('Content-type: %s\r\n' % type)
                self.push_text('\r\n')
                self.push_with_producer(file_producer(url))
        else:
            self.send_error(501, '%s method not implemented' % op)
        self.close_when_done()

# 创建file_producer
class file_producer(object):
    def __init__(self, filename, buffer_size = 1024):
        self.f = open(filename, 'rb')
        self.buffer_size = buffer_size

    def more(self):
        print('----more----')
        datas = self.f.read(self.buffer_size)
        if not datas:
            self.f.close()
        return datas

httpServer = async_http(('127.0.0.1', 8888))
asyncore.loop()
# fp = file_producer('testFile.txt')
# print(fp.more())