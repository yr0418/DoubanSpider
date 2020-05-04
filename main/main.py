# -*- coding: utf-8 -*-
# @File : test.py
# @Description：测试文件
# @Author : 杨睿
# @Time : 2020-04-30 17:35

from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import pymysql


# 1.入口主程序，爬取网页
def main():
    # 基础Url，起始页
    base_url = "https://movie.douban.com/top250?start="
    ask_url(base_url)
    # 1.爬取网页
    datalist = get_data(base_url)


# 2.获取网页数据，边爬边解析
def get_data(base_url):
    datalist = []
    for i in range(0, 10):
        url = base_url + str(i*25)
        html = ask_url(url)  # 获取一页的HTML网页源码
    return datalist


# 得到一个指定url的网页内容，返回字符串html，封装网页源码
def ask_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
    }
    # 模拟请求
    req = urllib.request.Request(url=url, headers=headers, method="GET")
    respond = urllib.request.urlopen(req)
    html = ""
    try:
        html = respond.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print("！！！ask_url，error.code: ", e.code)
        if hasattr(e, "reason"):
            print("！！！ask_url，error.reason: ", e.reason)
    return html


# 保存数据，将数据保存至MySQL数据库
def save_date(datalist):
    # 建立数据库连接
    db = pymysql.connect("localhost", "root", "yr19990418", "douban_movie")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用预处理语句创建表
    sql = """"""
    cursor.execute(sql)

    db.close()
    pass


if __name__ == '__main__':
    main()
