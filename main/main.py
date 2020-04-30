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

    # 1.爬取网页
    datalist = get_data(base_url)


# 2.获取网页数据，边爬边解析
def get_data(base_url):
    datalist = []
    pass
    return datalist


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
