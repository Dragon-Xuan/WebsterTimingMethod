# -*- coding:utf-8 -*-
'''
@Name:xmltest.py
@Author:Chen Tingxuan
@Date:2022/8/22 14:40
'''
import xml.sax
from xml.dom.minidom import parse
import xml.dom.minidom

class MovieHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        # 按照实际的xml里的各个标签来写
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""
    # 元素开始事件处理
    def startElement(self, name, attrs):
        self.CurrentData = name
        if name == 'movie':
            print("********Movie********")
            title = attrs["title"]
            print("Title ",title)

    # 元素结束事件处理
    def endElement(self, name):
        if self.CurrentData == "type":
            print("Type: ",self.type)
        elif self.CurrentData == "format":
            print ("Format:", self.format)
        elif self.CurrentData == "year":
            print ("Year:", self.year)
        elif self.CurrentData == "rating":
            print ("Rating:", self.rating)
        elif self.CurrentData == "stars":
            print  ("Stars:", self.stars)
        elif self.CurrentData == "description":
            print ("Description:", self.description)
        self.CurrentData = ""

    # 内容事件处理
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


if __name__ == "__main__":
    # 创建一个XMLReader
    parser = xml.sax.make_parser()
    #turn off namespaces
    parser.setFeature(xml.sax.handler.feature_namespaces,0)

    # 重写ContexHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)
    parser.parse("xmltest.xml")
    print("ok")


#     使用dom来解析包
    DOMTree = xml.dom.minidom.parse("xmltest.xml")
    collection = DOMTree.documentElement
    if collection.hasAttribute("shelf"):
        print ("Root element : %s" % collection.getAttribute("shelf"))

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
    print ("*****Movie*****")
    if movie.hasAttribute("title"):
        print ("Title: %s" % movie.getAttribute("title"))

    type = movie.getElementsByTagName('type')[0]
    print ("Type: %s" % type.childNodes[0].data)
    format = movie.getElementsByTagName('format')[0]
    print ("Format: %s" % format.childNodes[0].data)
    rating = movie.getElementsByTagName('rating')[0]
    print ("Rating: %s" % rating.childNodes[0].data)
    description = movie.getElementsByTagName('description')[0]
    print ("Description: %s" % description.childNodes[0].data)

