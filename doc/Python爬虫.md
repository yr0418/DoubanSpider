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
```

