# -*- coding:utf-8 -*-
'''
@Name:WebsterHttpServer.py
@Author:Chen Tingxuan
@Date:2022/8/8 11:08
'''
import json
import requests
import tornado.web
import tornado.httpserver
import tornado.ioloop
# options模块用于全局参数定义，存储，转换，从而不用将参数写死在程序中
import tornado.options




class WebSterTimingMethod():
    '''
    输入参数依次为
    ID:ID为该交通路口的编号
    N:交叉路口的信号相数
    Q:各相对应的标准车流量列表
    S:各相的饱和车流量列表
    L:各相的损失时间列表
    A:黄灯时间（默认3秒）
    R:全红时间（默认0秒）
    '''
    def __init__(self):
        self.ID = 0
        self.N = 0
        self.Q = 0
        self.S = 0
        self.L = 0
        self.A = 0
        self.R = 0
        self.C = 0
        self.TY = 0
        self.TL = 0

    def __updateparam(self,ID,N,Q,S,L,A=3,R=0):
        self.Id = ID
        self.N = N
        self.Q = Q
        self.S = S
        self.L = L
        self.A = A
        self.R = R


    #计算总损失时间
    def __calc_total_l(self):
        total_l = 0
        for l in self.L:
            total_l += l
        total_l += self.A*self.R
        self.TL = total_l
        return total_l

    #计算交叉口流量比综合Y
    def __calc_total_y(self):
        self.y = []
        total_y = 0
        for i in range(0,len(self.Q)):
            q = self.Q[i]
            s = self.S[i]
            y = q/s/self.N
            self.y.append(y)
            total_y += y
        self.TY = total_y
        return total_y

    # 计算红绿灯周期C
    def __calc_C(self):
        L = self.__calc_total_l()
        Y = self.__calc_total_y()
        try:
            C = int((1.5*L+5)/(1-Y))
        except ZeroDivisionError:
            C=0
            print("you can't divide by zero!")
        self.C = C
        return C


    # 处理三相信号时间融合
    def TimeFusion(self,G,Y,R):
        pass

    def TimingMethod(self,ID,N,Q,S,L,A=3,R=0):
        self.__updateparam(ID,N,Q,S,L,A,R)
        if not (N == len(Q) == len(S) == len(L)):
            return -1
        C = self.__calc_C()
        # 计算有效绿灯时间
        Ge = C - self.TL
        #计算各相位实际显示绿灯时间
        Method = []
        Id_Method_Map = {}
        for i in range(0,N):
            Mi = []
            Gi =int(Ge*(self.y[i]/self.TY) - A + L[i])
            Mi.append(Gi)
            Mi.append(A)
            Mi.append(C-Gi-A)
            Method.append(Mi)
            Id_Method_Map["junctionId"] = ID
            Id_Method_Map["duration"] = Method
        return Id_Method_Map










# 定义端口
tornado.options.define("port",default=9999,type=int)




class WebsterTimingServer(tornado.web.RequestHandler):
    # def get(self):
    #     # 获取数据
    #     data_list = json.loads(self.request.body)
    #     print(data_list)
    #     print(str(type(data_list)))
    #     # 处理数据
    #     WTM = WebSterTimingMethod()
    #     Methods = []
    #     for dict_data in data_list:
    #         print(dict_data["junctionId"])
    #         Method = WTM.TimingMethod(ID=dict_data["junctionId"],
    #                                   N=dict_data["phaseNum"],
    #                                   Q=dict_data["trafficFlowList"],
    #                                   S=dict_data["saturatedTrafficList"],
    #                                   L=dict_data["wastedTime"],
    #                                   A=dict_data["yellowTime"],
    #                                   R=dict_data["allRedTime"], )
    #         Methods.append(Method)
    #         # 返回数据
    #     print(Methods)
    #     self.write(json.dumps(Methods))
    #     print("ok")

    def post(self):

        # 获取数据
        data_list = json.loads(self.request.body)
        # print(data_list)
        # print(str(type(data_list)))
        # 处理数据
        WTM = WebSterTimingMethod()
        Methods = []
        for dict_data in data_list:
            # print(dict_data["junctionId"])
            Method = WTM.TimingMethod(ID=dict_data["junctionId"],
                                      N= dict_data["phaseNum"],
                                      Q= dict_data["trafficFlowList"],
                                      S= dict_data["saturatedTrafficList"],
                                      L= dict_data["wastedTime"],
                                      A= dict_data["yellowTime"],
                                      R= dict_data["allRedTime"],)
            Methods.append(Method)
            # 返回数据
        # print(Methods)
        self.write(json.dumps(Methods))
        print("ok")




if __name__ == "__main__":

    app = tornado.web.Application(handlers=[(r"/WebsterTiming",WebsterTimingServer)],autoreload=True)
    httpserver = tornado.httpserver.HTTPServer(app)
    print("prot: ")
    print(tornado.options.options.port)
    httpserver.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()



