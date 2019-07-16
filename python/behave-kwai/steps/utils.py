# -*- coding: utf-8 -*-

from behave import *
import time

def utils_darw(context):
    time.sleep(1)
    settings = context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/left_btn")')
    settings.click()

def utils_setting(context):
    time.sleep(1)
    setting = context.driver.find_element_by_android_uiautomator('new UiSelector().text("设置")')
    setting.click()

def utils_tab2(context):
    time.sleep(1)
    tab2 = context.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/"
                                                "android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/"
                                                "android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/"
                                                "android.widget.RelativeLayout[2]/android.widget.ImageView[1]")
    tab2.click()
    tab2.click()

def utils_square_more(context):
    time.sleep(1)
    square_more = context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/iv_operation")')
    square_more.click()

def utils_square_more_1(context):
    time.sleep(1)
    square_more_1 = context.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/"
        "android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.TextView[1]")
    square_more_1.click()

def utils_square_more_2(context):
    time.sleep(1)
    square_more_2 = context.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/"
        "android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.TextView[2]")
    square_more_2.click()

def utils_button1(context):
    time.sleep(1)
    button1 = context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/button1")')

    # button1 = context.driver.find_element_by_id('com.kwai.sogame:id/button1')
    button1.click()
