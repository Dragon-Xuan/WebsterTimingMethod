# -*- coding:utf-8 -*-
'''
@Name:WebsterTimingMethod.py
@Author:Chen Tingxuan
@Date:2022/8/4 15:33
'''
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

    # {"junctionId":"","duration": [[18, 3, 29], [15, 3, 32], [6, 3, 41]]}
    #
    # {"durationNum":3,}


if __name__ == "__main__":
    webstertimingmethod = WebSterTimingMethod()

    Method = webstertimingmethod.TimingMethod(ID=12,
                                              N=3,
                                              Q=[1200,1000,800],
                                              S=[1800,1800,1800],
                                              L=[5.2,5.2,3.2],
                                              A=3,
                                              R=0)
    if (Method != -1):
        print("交通信号周期为:"+str( webstertimingmethod.C))
        print(Method)

    else:
        print("input illegal")















