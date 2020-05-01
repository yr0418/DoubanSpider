# -*- coding: utf-8 -*-
# @File : UrllibTest.py
# @Description：urllib包的测试文件
# @Author : 杨睿
# @Time : 2020-04-30 23:01

import urllib.request  # 发送get/post请求
import urllib.parse  # 解析器，解析上传服务器的数据

# 模仿get请求，注意 User-Agent为："Python-urllib/3.7"，直接表明自己是使用 urllib模拟的请求
respond = urllib.request.urlopen('http://www.baidu.com')
# 显示返回的这个网页的对象
print(respond)
# 显示返回的网页，即构成这个网页的html5代码，使用utf-8解析网页编码，这样能返回一个正常的网页源代码展示
print(respond.read().decode('utf-8'))


# 模仿一个post请求，访问的网址为：httpbin.org。注意 User-Agent为："Python-urllib/3.7"，直接表明自己是使用 urllib模拟的请求
data = bytes(urllib.parse.urlencode({'hello': 'world'}), encoding='utf-8')  # urlencode()封装数据，parse()对封装的数据进行解析
respond = urllib.request.urlopen('http://httpbin.org/post', data=data)  # data用于封装必要的参数，
print(respond.read().decode('utf-8'))


# 请求限时操作，超时会抛出异常：urllib.error.URLError:<urlopen error timed out>。防止程序卡死
try:
    respond = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
    print(respond.read().decode('utf-8'))
except urllib.error.URLError as e:
    print('time out')


# 显示返回的网页对象中指定的信息
respond = urllib.request.urlopen('http://www.baidu.com')
# print(respond.getheaders())  # 列表形式显示所有的头部信息
# print(respond.getheader('Server'))  # 显示指定的头部信息

