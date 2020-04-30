# Python爬虫基础

---

> 本项目爬取豆瓣电影排名前250名的电影数据
>
> url地址：https://movie.douban.com/top250

[TOC]

## 1.需要使用的包

---

```python
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，文字匹配
import urllib.request, urllib.error  # 制定url，获取网页数据
import xlwt  # 进行Excel操作
import pymysql  # 操作MySQL数据库
```

---

## 2.原始程序

```python
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
    datalist = get_data(base_url)


# 2.解析数据，边爬边解析
def get_data(base_url):
    datalist = []
    pass
    return datalist


# 3.保存数据，将数据保存至MySQL数据库
def save_date(datalist):
    pass


if __name__ == '__main__':
    main()
```

