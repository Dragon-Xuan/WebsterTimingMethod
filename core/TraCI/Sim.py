# -*- coding:utf-8 -*-
'''
@Name:Sim.py
@Author:Chen Tingxuan
@Date:2022/8/17 16:21
'''
import traci
import sys
class Sim():
    def __init__(self,sumo_config,GUI=False,sumo=traci):
        self.sumo = sumo
        self.sumo_config = sumo_config
        self.launch_env_flag = False
        self.GUI = GUI
        self.steps = 0

    def launchEnv(self):
        # 开始模拟（通过traci来获取其中的数据）
        if self.GUI:
            sumo_gui = 'sumo-gui'
        else:
            sumo_gui = 'sumo'

        traci.start([sumo_gui,
                     "-c",self.sumo_config,
                     "--no-warnings",
                     "--seed",
                     "2"])
        self.launch_env_flag = True

    def close(self):

        traci.close()
        self.launch_env_flag = False
        sys.stdout.flush()

    def reset(self):
        # 关闭当前环境，并开启一个新的环境
        self.close()
        self.launchEnv()

    def getEdgeVehicleNumber(self,EdgeId):
        return self.sumo.edge.getLastStepVehicleNumber(edgeID=EdgeId)

    def setRedYellowGreenState(self,tlsid,state):
        self.sumo.trafficlight.setRedYellowGreenState(tlsID=tlsid,state=state)


    def step(self):
        steps = 0
        assert self.launch_env_flag
        # 当路网里面还有车
        while self.sumo.simulation.getMinExpectedNumber()>0:
            self.sumo.simulationStep()
            steps = steps+1
        self.steps = steps


    def runSim(self):

        # 初始化环境
        self.launchEnv()
        # 进行模拟
        self.step()
        # 关闭环境
        self.close()

if __name__ == '__main__':
    SC1 = "D:\Document\CodeFile\python\WebsterTimingMethod\Resource\MAP\cross_web\sumocfg_web\cross_web.sumocfg"
    SC2 = "D:\Document\CodeFile\python\WebsterTimingMethod\Resource\MAP\cross_web\sumocfg_static\cross_static.sumocfg"
    sumo_sim1 = Sim(sumo_config=SC1,GUI=False)
    sumo_sim2 = Sim(sumo_config=SC2,GUI=False)
    sumo_sim1.runSim()
    sumo_sim2.runSim()
    print(sumo_sim1.steps)
    print(sumo_sim2.steps)






