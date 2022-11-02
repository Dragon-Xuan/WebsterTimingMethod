# -*- coding:utf-8 -*-
'''
@Name:client.py
@Author:Chen Tingxuan
@Date:2022/8/8 15:01
'''
import requests
import json
if __name__ == "__main__":
    data = [
    {
        "trafficFlowList":[
            1432,
            646,
            1246,
            705
        ],
        "junctionId":"M10001",
        "allRedTime":0,
        "yellowTime":3,
        "maxDurationTime":100,
        "minDurationTime":40,
        "saturatedTrafficList":[
            1534,
            1534,
            1534,
            1534
        ],
        "wastedTime":[
            1.4,
            1.4,
            1.4,
            1.4
        ],
        "phaseNum":4
    },
    {
        "maxDurationTime": 100,
        "minDurationTime": 40,
        "trafficFlowList":[
            1225,
            691,
            1387,
            756
        ],
        "junctionId":"M10002",
        "allRedTime":0,
        "yellowTime":3,
        "saturatedTrafficList":[
            1443,
            1443,
            1443,
            1443
        ],
        "wastedTime":[
            2,
            2,
            2,
            2
        ],
        "phaseNum":4
    },
    {
        "maxDurationTime": 100,
        "minDurationTime": 40,
        "trafficFlowList":[
            1406,
            515,
            1234,
            745
        ],
        "junctionId":"M10003",
        "allRedTime":0,
        "yellowTime":3,
        "saturatedTrafficList":[
            1338,
            1338,
            1338,
            1338
        ],
        "wastedTime":[
            2.6,
            2.6,
            2.6,
            2.6
        ],
        "phaseNum":4
    },
    {
        "maxDurationTime": 100,
        "minDurationTime": 40,
        "trafficFlowList":[
            1429,
            575,
            1364,
            589
        ],
        "junctionId":"M10004",
        "allRedTime":0,
        "yellowTime":3,
        "saturatedTrafficList":[
            1537,
            1537,
            1537,
            1537
        ],
        "wastedTime":[
            1.4,
            1.4,
            1.4,
            1.4
        ],
        "phaseNum":4
    },
    {
        "maxDurationTime": 100,
        "minDurationTime": 40,
        "trafficFlowList":[
            1479,
            678,
            1347,
            505
        ],
        "junctionId":"M10005",
        "allRedTime":0,
        "yellowTime":3,
        "saturatedTrafficList":[
            1390,
            1390,
            1390,
            1390
        ],
        "wastedTime":[
            2.5,
            2.5,
            2.5,
            2.5
        ],
        "phaseNum":4
    },
    {
        "maxDurationTime": 100,
        "minDurationTime": 40,
        "trafficFlowList":[

            743,
            1365,
            785
        ],
        "junctionId":"M10006",
        "allRedTime":0,
        "yellowTime":3,
        "saturatedTrafficList":[
            1275,
            1275,
            1275,
            1275
        ],
        "wastedTime":[
            3,
            3,
            3,
            3
        ],
        "phaseNum":4
    },
    {
        "maxDurationTime": 100,
        "minDurationTime": 40,
        "trafficFlowList":[
            1303,
            745,
            1207,
            650
        ],
        "junctionId":"M10007",
        "allRedTime":0,
        "yellowTime":3,
        "saturatedTrafficList":[
            1693,
            1693,
            1693,
            1693
        ],
        "wastedTime":[
            2.7,
            2.7,
            2.7,
            2.7
        ],
        "phaseNum":4
    },
    {
        "maxDurationTime": 100,
        "minDurationTime": 40,
        "trafficFlowList":[
            1465,
            669,
            1266,
            557
        ],
        "junctionId":"M10008",
        "allRedTime":0,
        "yellowTime":3,
        "saturatedTrafficList":[
            1523,
            1523,
            1523,
            1523
        ],
        "wastedTime":[
            1.4,
            1.4,
            1.4,
            1.4
        ],
        "phaseNum":4
    },
    {
        "maxDurationTime": 100,
        "minDurationTime": 40,
        "trafficFlowList":[
            1401,
            598,
            1414,
            530
        ],
        "junctionId":"M10009",
        "allRedTime":0,
        "yellowTime":3,
        "saturatedTrafficList":[
            1341,
            1341,
            1341,
            1341
        ],
        "wastedTime":[
            1.5,
            1.5,
            1.5,
            1.5
        ],
        "phaseNum":4
    },
    {
        "maxDurationTime": 100,
        "minDurationTime": 40,
        "trafficFlowList":[
            1452,
            560,
            1368,
            651
        ],
        "junctionId":"M100010",
        "allRedTime":0,
        "yellowTime":3,
        "saturatedTrafficList":[
            0,
            0,
            0,
            0
        ],
        "wastedTime":[
            2.7,
            2.7,
            2.7,
            2.7
        ],
        "phaseNum":4
    }
]
    data2 =   [  {
        "trafficFlowList":[
            1,
            1,
            1,
            1
        ],
        "junctionId":"MI10097",
        "maxDurationTime":0,
        "minDurationTime":0,
        "trafficMap":{
            "MI10894":4,
            "D103201":5,
            "D103200":5,
            "MI10888":2,
            "MI10891":4
        },
        "allRedTime":0,
        "yellowTime":3,
        "saturatedTrafficList":[
            1,
            1,
            1,
            1
        ],
        "wastedTime":[
            1,
            1,
            1,
            1
        ],
        "phaseNum":4
    }]
    json_data = json.dumps(data)
    x = requests.post(url='http://localhost:9999/WebsterTiming',
                      data=json_data)
    print(x.status_code)
    print(x.reason)
    print(x.apparent_encoding)
    print(x.text)


