# -*- coding: utf-8 -*-

from appium import webdriver
import time


def before_all(context):
    # context.config.setup_logging()
    pass


def before_feature(context, feature):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = 'A59s_11_A12_180302'
    desired_caps['autoGrantPermissions'] = True
    desired_caps['appPackage'] = 'com.kwai.sogame'
    desired_caps['udid'] = context.userdata.get("udid")
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['appActivity'] = 'com.kwai.sogame.combus.launch.SogameLaunchActivity'
    desired_caps['systemPort'] = 8201
    desired_caps['noReset'] = True
    # desired_caps['app'] = '/Users/huangzetao/Desktop/Sogame-2.5.22-release_DEFAULT.apk'   'HQ5HLFW899999999'

    context.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
