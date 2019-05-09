# -*- coding: utf8 -*-
import os
import time
import sys
from pylib import android_commands
from perf import surface_stats_collector
from adb_tool import *

resultList = []
# deviceText = os.popen('adb devices')
# textList = deviceText.readlines()
# deviceName = textList[1].split()[0]
# adb = android_commands.AndroidCommands(deviceName)

device = AdbTools()
collector = surface_stats_collector.SurfaceStatsCollector(device,0,"com.kwai.sogame/com.kwai.sogame.combus.launch.SogameMainActivity")
collector.DisableWarningAboutEmptyData()
collector.Start()
# for i in range(50):    #循环50次，主要方便自己的实现，其他实现方法请另行实现；
#     time.sleep(0.3)
#     results = collector.SampleResults()
#     if not results:
#         pass
#     else:
#         resultList.append(int(results[0].value))
#         results[0].print_str()

for i in range(50):
    time.sleep(1)
    results = collector.SampleResults()
    for i in results:
        if i.name == 'avg_surface_fps':
            print(i.value)
    #
    # resultList.append(results[0].value)
    # print(resultList)

# print(results)

collector.Stop()
# a = resultList[3:-3]
# print u"平均值："+str(float(sum(a)/len(a)))+u" ; 最小值："+str(min(a))