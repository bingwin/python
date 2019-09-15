# -*- coding: utf-8 -*-

from behave import *
import time
import utils

# context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/phone_tv")')
# com.kwai.sogame:id/draw_avatar

@given(u'个人资料_点击个人资料')
def draw_avatar(context):
    time.sleep(1)
    raw_avatar = context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/draw_avatar")')
    raw_avatar.click()

@given(u'个人资料_编辑个人资料')
def tv_edit(context):
    time.sleep(1)
    tv_edit = context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/tv_edit")')
    tv_edit.click()

@given(u'个人资料_点击头像')
def sdv_avatar(context):
    time.sleep(1)
    sdv_avatar = context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/sdv_avatar")')
    sdv_avatar.click()

@given(u'个人资料_点击从相册选择')
def choose_portrait(context):
    time.sleep(1)
    text1 = context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/text1")')
    text1.click()

@given(u'个人资料_点击第一张图片')
def choose_portrait_2(context):
    time.sleep(1)
    choose_portrait_2 = context.driver.find_element_by_xpath(
        "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/"
        "android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/"
        "android.widget.FrameLayout[1]/android.widget.ImageView[1]")
    choose_portrait_2.click()

@given(u'个人资料_点击确定')
def bt_ok(context):
    time.sleep(1)
    bt_ok = context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/bt_ok")')
    bt_ok.click()

@given(u'个人资料_点击完成')
def tv_right(context):
    time.sleep(2)
    tv_right = context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/tv_right")')
    tv_right.click()

@given(u'个人资料_返回')
def left_iv_btn(context):
    time.sleep(4)
    left_iv_btn = context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/left_iv_btn")')
    left_iv_btn.click()

@given(u'个人资料_好友')
def icon_iv(context):
    time.sleep(1)
    iv_close_invite = context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/draw_friend_add")')
    iv_close_invite.click()

# @given(u'个人资料_切换到广场')
# def tab2(context):
#     utils.utils_tab2(context)








