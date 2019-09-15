# -*- coding: utf-8 -*-

from appium import webdriver
import allure
import allure_commons._allure
from allure_behave.hooks import allure_report
import time

def before_all(context):
    # context.config.setup_logging()
    pass

def before_feature(context, feature):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    # desired_caps['deviceName'] = 'ONEPLUSA5000_6e48b8db'
    desired_caps['deviceName'] = 'test'         # 可以随便起
    desired_caps['autoGrantPermissions'] = True
    desired_caps['appPackage'] = 'com.kwai.sogame'
    # desired_caps['udid'] = context.userdata.get("udid")   devices id 6e48b8db
    # desired_caps['udid'] = context.config.userdata.get("udid")
    # desired_caps['udid'] = context.config.userdata["udid"]

    desired_caps['automationName'] = 'UiAutomator2'
    # desired_caps['appActivity'] = 'com.kwai.sogame.combus.launch.SogameLaunchActivity'
    desired_caps['appActivity'] = 'com.kwai.sogame.combus.launch.SogameMainActivity'
    desired_caps['systemPort'] = 8201
    desired_caps['noReset'] = True
    # desired_caps['app'] = '/Users/huangzetao/Desktop/Sogame-2.5.22-release_DEFAULT.apk'   'HQ5HLFW899999999'

    context.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

# def after_scenario(context, scenario):
    # allure.attac