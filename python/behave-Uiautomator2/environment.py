# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time
import os

def uninstall(packageName):
    os.popen("adb wait-for-device")
    print("start uninstall...")
    os.popen("adb uninstall %s" % packageName)

def install(filename):
    print("install...")
    os.popen("adb install %s" % filename)

def before_all(context):
    d = u2.connect_usb('6e48b8db')

    apk = "com.smile.gifmaker"

    uninstall(apk)

    install("/Users/huangzetao/Desktop/快手app包/kwai-android-test-gifmakerhuidu-6.8.1.99999-回测.apk")

    d.app_start(apk)

    print("success")

    # time.sleep(2)
    #
    # d(resourceId="com.smile.gifmaker:id/left_btn").click()
    #
    # time.sleep(1)
    #
    # d(resourceId="com.smile.gifmaker:id/tv_game_center").click()

# def before_feature(context, feature):

