# -*- coding:utf-8 -*-
'''
@Name:DataAnalysis.py
@Author:Chen Tingxuan
@Date:2022/8/22 13:58
'''

# 分析检测器的结果,检测器的结果很多，选定需要的数据

import xml.sax
from xml.dom.minidom import parse
import xml.dom.minidom

# 获得单条道路信息 laneid
import traci


class Detector_Analysis():
    def __init__(self):
        self.doce1 = ''
        self.doce2 = ''

    def E1init(self,e1):
        self.doce1 = e1

    def E2init(self,e2):
        self.doce2 = e2



if __name__ == "__main__":
    DOMTree1 = xml.dom.minidom.parse("../../Resource/MAP/cross_web/e1output.xml")
    detectore1 = DOMTree1.documentElement
    intervals = detectore1.getElementsByTagName("interval")
    for interval in intervals:
        if interval.hasAttribute("flow"):
            print("Flow: %s"% interval.getAttribute("flow"))
        else:
            print("none")