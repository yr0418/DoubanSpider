# -*- coding: utf-8 -*-
# @File : UrllibTest2.py
# @Description：代码模拟post/get请求，伪装成浏览器骗过网站的User-Agent检测
# @Author : 杨睿
# @Time : 2020-05-01 13:07

import urllib.request  # 发送get/post请求
import urllib.parse  # 解析器，解析上传服务器的数据

# url = 'http://httpbin.org/post'
url = "https://movie.douban.com/top250"
# 模拟浏览器发送的头文件：Request Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
}
# 模拟请求
req = urllib.request.Request(url=url, headers=headers, method="GET")

respond = urllib.request.urlopen(req)
print(respond.getheaders())


