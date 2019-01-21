#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: request_test.py
# @Time: 2019-1-21 13:45

import requests

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
headers_temp = {
    'User-Agent': user_agent
}
cookies_temp = 'BAIDUID=494D9F77445DE99F1F156CDC26D3AF75:FG=1;'
res = requests.get('http://www.baidu.com', headers=headers_temp, cookies='cookies_temp')
print(res.content.decode())

# 带有查询参数的
queryParam = {
    'Keywords':
        'blog: qiyeboa',
        'pageindex': 2
}
result = requests.get('http://www.baidu.com', params=queryParam)
print(result.url)

# 自动处理cookies的方式
loginUrl = 'http://xxxxxxx/login'
sess = requests.Session()
# 首先访问登录界面，作为游客，服务器会分配一个cookie
r = sess.get(loginUrl, allow_redirects=True)
datas = {
    'username': 'dwedwe',
    'password': 'xscsdc'
}
# 向登录链接发送post请求，验证通过，转为会员
r = sess.post(loginUrl, data=datas, allow_redirects=True)
print(r.text)

# 使用代理
proxies_temp = {
    'http': '10.20.2.1:8080',
    'https': '12.26.20.5:8080'
}
request = requests.get(loginUrl, proxies=proxies_temp)