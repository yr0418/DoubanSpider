# -*- coding: utf-8 -*-
# @File : spider.py
# @Description：爬虫主程序
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
    save_date(datalist)


# 2.获取网页数据，边爬边解析
def get_data(base_url):
    datalist = []
# 正则表达式如下：
    # 影片排名
    movie_ranking = re.compile(r'<em class="">(\d*)</em>')
    # 影片详情链接
    movie_link = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，表示规则（字符串的模式）

    # 影片图片
    movie_img_src = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S 让换行符包含在字符中

    # 影片片名
    movie_title = re.compile(r'<span class="title">(.*)</span>')

    # 影片评分
    movie_rating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')

    # 找到评价人数
    movie_judge_num = re.compile(r'<span>(\d*)人评价</span>')

    # 找到概况
    movie_inq = re.compile(r'<span class="inq">(.*)</span>')

    # 找到影片的相关内容：导演，主演，电影类型
    movie_bd = re.compile(r'<p class="">(.*?)</p>', re.S)

    for i in range(0, 10):
        url = base_url + str(i*25)
        html = ask_url(url)  # 获取一页的HTML网页源码
        soup = BeautifulSoup(html, "html.parser")  # 解析数据

        # 在网页源码中，电影信息封装在 类名为 item 的 div 标签中
        for item in soup.find_all('div', class_="item"):
            movie_data = []  # 使用列表来封装一部电影的信息
            item = str(item)
            # print(item)
            # 影片排名
            ranking = re.findall(movie_ranking, item)[0]
            # print(ranking)
            movie_data.append(ranking)

            # 影片详情的链接
            link = re.findall(movie_link, item)[0]
            movie_data.append(link)  # 添加电影详情链接

            # 影片封面，保存图片链接
            img_src = re.findall(movie_img_src, item)[0]
            movie_data.append(img_src)  # 添加电影封面链接

            # 影片名，片名可能只有一个中文名，没有外国名
            titles = re.findall(movie_title, item)
            if len(titles) == 2:
                zh_title = titles[0]  # 添加中文名
                movie_data.append(zh_title)
                en_title = titles[1].replace("/", "")  # 去掉无关的符号
                movie_data.append(en_title)  # 添加英文名
            else:
                movie_data.append(titles[0])  # 添加中文名
                movie_data.append(' ')  # 外国名字留空

            # 影片评分
            rating = re.findall(movie_rating, item)[0]
            movie_data.append(rating)  # 添加评分

            # 评价人数
            judge_num = re.findall(movie_judge_num, item)[0]
            movie_data.append(judge_num)  # 提加评价人数

            # 电影概况，可能出现没有概况的情况
            inq = re.findall(movie_inq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")  # 去掉句号
                movie_data.append(inq)  # 添加概述
            else:
                movie_data.append(" ")  # 留空

            # 电影相关信息：导演，主演，电影类型
            bd = re.findall(movie_bd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br/>
            bd = re.sub('/', " ", bd)  # 替换/
            movie_data.append(bd.strip())  # 去掉前后的空格

            # 把处理好的一部电影信息放入datalist
            datalist.append(movie_data)

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
    # 当表存在时删除表，重新建立一张新表
    drop_sql = "DROP TABLE IF EXISTS `movie250`"
    cursor.execute(drop_sql)
    create_sql = """CREATE TABLE movie250(
                    ranking bigint (255) not null,
                    link varchar (255), 
                    img_src varchar (255),
                    zh_title varchar (255),
                    en_title varchar (255),
                    rating varchar (255),
                    judge_num varchar (255),
                    inq varchar (255),
                    bd varchar (255),
                    primary key(ranking)
                    )"""
    cursor.execute(create_sql)

    # 使用预处理语句创建表
    for data in datalist:
        for index in range(len(data)):
            data[index] = '"' + data[index] + '"'
        sql = """insert into movie250 
                 (ranking,link,img_src,zh_title,en_title,rating,judge_num,inq,bd) values(%s)""" % ",".join(data)
        # print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
    db.close()


if __name__ == '__main__':
    main()
