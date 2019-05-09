# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import animation
import re
import os

def getTotalPss():
    lines = os.popen("adb shell dumpsys meminfo com.kwai.game.doll ").readlines() #逐行读取
    total = "TOTAL"
    for line in lines:
        if re.findall(total, line): # 找到TOTAL 这一行
            lis = line.split(" ")  #将这一行，按空格分割成一个list
            while '' in lis:       # 将list中的空元素删除
                lis.remove('')
            return lis[1] #返回总共内存使用


def getCpu():
    li = os.popen("adb shell top -m 100 -n 1 -s cpu").readlines()
    name = "com.kwai.game.doll"
    for line in li:
        if re.findall(name,line):
            cuplist = line.split(" ")
            if cuplist[-1].strip() == 'com.kwai.game.doll':
                while '' in cuplist:       # 将list中的空元素删除
                    cuplist.remove('')
                return float(cuplist[2].strip('%')) #去掉百分号，返回一个float



fig = plt.figure()
ax1 = fig.add_subplot(2,1,1,xlim=(0, 100), ylim=(0, 1000))
# ax2 = fig.add_subplot(2,1,2,xlim=(0, 100), ylim=(0, 100))
ax2 = fig.add_subplot(2,1,2,xlim=(0, 100), ylim=(0, 50))

line, = ax1.plot([], [], lw=2)
line2, = ax2.plot([], [], lw=2)
x = []
y = []
y2 = []
def init():
    line.set_data([], [])
    line.set_data([], [])
    return line,line2
def getx():
    t = "0"
    return t

def animate(i):
    x.append(int(getx())+i)
    y.append(int(getTotalPss())/1024) #每执行一次去获取一次值加入绘制的data中
    y2.append(getCpu())
    print x,y
    line.set_data(x,y)
    line2.set_data(x,y2)
    return line,line2

anim1 = animation.FuncAnimation(fig, animate, init_func=init,  frames=1000, interval=30)
plt.show()
