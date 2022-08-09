# Webster 配时法
> Webster配时法是最经典的进口道延误计算模型，其目标是为了最优化总延误而计算得出一套红绿灯路口的配时方案
### 算法模型
本项目基于python实现了基本的Webster配时法的算法模型，模型算法在Webster文件夹下的WebsterTimingMethod.py文件内  

```buildoutcfg
    # 创建一个对象  
    webstertimingmethod = WebSterTimingMethod()
    # 输入对应参数
    Method = webstertimingmethod.TimingMethod(ID=12,
                                              N=3,
                                              Q=[1200,1000,800],
                                              S=[1800,1800,1800],
                                              L=[5.2,5.2,3.2],
                                              A=3,
                                              R=0)
    
    输入参数依次为
    ID:ID为该交通路口的编号
    N:交叉路口的信号相数
    Q:各相对应的标准车流量列表
    S:各相的饱和车流量列表
    L:各相的损失时间列表
    A:黄灯时间（默认3秒）
    R:全红时间（默认0秒）
```

### Http服务器
并且基于该模型基于tornado 这个python-web框架实现了Http服务器，可以根据输入参数给出实际的配时方案返回，具体代码见Webster文件夹下的WebsterHttpServer.py文件

```buildoutcfg
# 定义端口,默认为9999
tornado.options.define("port",default=9999,type=int)
```