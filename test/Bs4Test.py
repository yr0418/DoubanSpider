# -*- coding: utf-8 -*-
# @File : Bs4Test.py
# @Description：测试 bs4 中的 BeautifulSoup，文档解析
# @Author : 杨睿
# @Time : 2020-05-04 21:40

"""
BeautifulSoup：将复杂的 HTML 文档转换成一个复杂的树形结构，每一个节点都是 Python 对象，所有的对象可以归为 4 种：
- Tag：标签及其内容，拿到第一个与其匹配的标签的内容。
- NavigableString：标签里的内容，即字符串部分
- BeautifulSoup: 即 BeautifulSoup 类型的对象：bs
- Comment：注释，获取匹配到的第一个标签的内容时，如果这个内容是一个注释，则该类型会自动去掉注释
"""

from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")  # 以字节流的方式读取文件，rb：字节流读取
html = file.read()
bs = BeautifulSoup(html, "html.parser")  # 使用 HTML 解析器，解析 html 这个文档

# -Tag：标签及其内容，拿到第一个与其匹配的标签的内容。
# 打印文件中第一个与 “title” 匹配的标签的全部内容。
# type(bs.title) = bs4.element.Tag
print(bs.title)

# - NavigableString：标签里的内容，即字符串部分
# 打印标签 title 中的内容：百度一下，你就知道。
# type(bs.title.string) = bs4.element.NavigableString
print(bs.title.string)
print(type(bs.title.string))

# 打印第一个匹配到的 a 标签中的属性，以字典形式保存属性
print(bs.a.attrs)

# - Comment：注释，获取匹配到的第一个标签的内容时，如果这个内容是一个注释，则该类型会自动去掉注释
# type(bs.a.string) = bs4.element.Comment
print(bs.a.string)
print(type(bs.a.string))



