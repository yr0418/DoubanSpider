# -*- coding: utf-8 -*-
# @File : test.py
# @Description：测试文件
# @Author : 杨睿
# @Time : 2020-04-30 17:35

from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error


# 入口主程序
def main():
    # 基础Url，起始页
    base_url = "https://movie.douban.com/top250?start="

    # 1.爬取网页
    datalist = get_data(base_url)


# 获取网页数据
def get_data(base_url):
    datalist = []

    # 2.解析数据，边爬边解析
    pass
    return datalist


# 保存数据，将数据保存至MySQL数据库
def save_date():
    pass


if __name__ == '__main__':
    main()
