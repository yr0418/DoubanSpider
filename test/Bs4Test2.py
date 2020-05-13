# -*- coding: utf-8 -*-
# @File : Bs4Test2.py
# @Description：BeautifulSoup 中 4 种对象的使用
# @Author : 杨睿
# @Time : 2020-05-04 22:29

from bs4 import BeautifulSoup
import re

file = open("./baidu.html", "rb")  # 以字节流的方式读取文件，rb：字节流读取
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")  # 使用 HTML 解析器，解析 html 这个文档

# 文档的遍历
# 将 head 标签中包括的所有标签及其内容，以列表元素的形式保存到一个列表中。单个标签对应单个元素。（具体看打印结果）
# print(bs.head.contents)


# 文档的搜索

# 1、find_all
# (1)字符串过滤：会查找与字符串 “a” 完全匹配的 标签。列表中的元素为 标签及其内容
# t_list = bs.find_all("a")


# (2)正则表达式搜索
# print(bs.find_all(re.compile("a")))

# (3)根据自定义的方法要求进行匹配
# 判断标签是否具有 name 属性
# def name_is_exists(tag):
#     return tag.has_attr("name")
# 根据 name_is_exists() 这个方法的要求进行标签的匹配
# t_list = bs.find_all(name_is_exists)


# 2、kwargs：根据参数进行查询
# 查询 标签中 id="head" 的标签及其内容
# t_list = bs.find_all(id="head")


# 3、文本参数 text，根据指定的文本内容搜索匹配的文本
# 参数值可以是列表，也可以是正则表达式
# t_list = bs.find_all(text=["地图", "贴吧", "新闻"])
# t_list = bs.find_all(text=re.compile("\d"))


# 4、选择器
# (1) 通过 标签名 来查找
# t_list = bs.select("title")

# (2) 通过标签的 类名 来查找，注意，使用 “.” 来标识参数指的是 类名
# t_list = bs.select(".mnav")

# (3) 通过标签的 id 来查找，注意，使用 “#” 来标识参数指的是 id
# t_list = bs.select("#u1")

# (4) 通过 指定标签名以及属性值 来查找
# t_list = bs.select("a[class='bri']")

# (5) 通过标签的层级来进行查找
# t_list = bs.select("div > div > a[class='bri']")

# (6) 通过 兄弟节点 进行查找
# 查找 与标签类名为 mnav 的标签 同级的，且类名为 bri 的标签
t_list = bs.select(".mnav ~ .bri")
for item in t_list:
    print(item)


