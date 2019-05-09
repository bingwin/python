# -*- coding:utf-8 -*-

import os
import platform

class AdbTools(object):
    # 如果不想让实例中的内部属性被外部属性访问，则把
    # name
    # 和
    # score
    # 变成
    # __name
    # 和
    # __score
    # 即可，如下代码所示
    # https: // blog.csdn.net / hansry / article / details / 79639676

    def __init__(self,device_id=''):
        self.__system = platform.system()
        self.__find = ''
        self.__command = 'adb'
        self.__device_id = device_id
        self.__device = None
        self.__client = None
        # self.__connect_device()
        # self.test = test

    def adb(self, args):
        """
        执行adb命令
        :param args:参数
        :return:
        """
        cmd = "%s %s %s" % (self.__command, self.__device_id, str(args))
        return os.popen(cmd)

    def get_devices(self):
        """
        获取设备列表
        :return:
        """
        l = self.adb('devices').readlines()
        i = l[1].split()
        s = i[0]
        return s
        # return (i.split()[0] for i in l if 'devices' not in i and len(i) > 5)

    # def device(self):
    #     if self.__device is None:
    #         self.__connect_device()
    #     return self.__device®

    # def __create_client(self):
    #     """
    #     use lib:pure-python-adb
    #     :return:
    #     """
    #     self.__client = AdbClient(self.__ip, self.__port)
    #
    # def __connect_device(self):
    #     """
    #     via self.__client make a connection with device_id
    #     :return:device
    #     """
    #     try:
    #         devices = self.__client.devices()
    #         if self.__device_id == "" and devices:
    #             self.__device = devices[0]
    #         else:
    #             self.__device = self.__client.device(self.__device_id)
    #     except:
    #         self.__device = None

    def pr(self):
        print(self.__device_id)



adb_1 = AdbTools()
print(adb_1.get_devices())

# adb_1.pr()
# i = adb_1.adb('devices').readlines()
# print(i)
# l = i[1]
# print(l)
# i = adb_1.device()ß
# print(i)
