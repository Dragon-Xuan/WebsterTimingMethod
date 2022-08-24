# -*- coding:utf-8 -*-
'''
@Name:sumo.py
@Author:Chen Tingxuan
@Date:2022/8/12 14:36
'''

import os,sys
import traci
import traci.constants as tc
if __name__ == "__main__":
    # 加载sumo tools路径到系统路径中去
    if 'SUMO_HOME' in os.environ:
        tools = os.path.join(os.environ['SUMO_HOME'],"tools")
        sys.path.append(tools)

    else:
        sys.exit("please declare environment variable 'SUMO_HOME'")

    #   命令行启动sumo/sumo-gui
    sumoBinary = "sumo-gui"
    # 确定sumocfg文件的位置
    sumoCfg = os.path.join(os.environ["SUMO_HOME"],"MAP","lympics","sumolympics.sumocfg")
    sumoCfg = "D:\\Document\\CodeFile\\python\\WebsterTimingMethod\\Resource\\MAP\\cross_web\\cross_web.sumocfg"
    sumoCmd = [sumoBinary,"-c",sumoCfg]
    traci.start(sumoCmd)
    traci.simulationStep(50000)
    # 如何设计指标进行统计

    # 关闭仿真
    traci.close()



