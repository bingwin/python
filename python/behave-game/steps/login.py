# -*- coding: utf-8 -*-

from behave import *
import time
import utils
import os


@given(u'登录测试_获取登录按钮')
def phone_tv_login(context):
    phone_tv_login = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/phone_tv")')
    phone_tv_login.click()


@given(u'登录测试_输入手机号:"{phone}"')
def phone_user(context, phone):
    phone_user = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/login_phone_input")')
    time.sleep(2)
    phone_user.click()
    # phone_user.clear()
    time.sleep(1)
    phone_user.set_value(str(phone))
    time.sleep(2)


@given(u'登录测试_进入验证码界面')
def login_phone_container(context):
    login_phone_container = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/login_phone_next")')
    login_phone_container.click()


@given(u'登录测试_输入验证码:"{verification}"')
def login_code_input(context, verification):
    time.sleep(2)
    login_code_input = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/login_code_input")')
    login_code_input.set_value(str(verification))
    time.sleep(1)
    print("输入验证码已测试")


@given(u'登录测试_拉取抽屉')
def darw(context):
    utils.utils_darw(context)


@given(u'登录测试_点击设置')
def setting(context):
    utils.utils_setting(context)


@given(u'登录测试_账号绑定')
def tv_desc(context):
    time.sleep(1)
    tv_desc = context.driver.find_element_by_android_uiautomator('new UiSelector().text("帐号绑定")')
    tv_desc.click()


@given(u'登录测试_返回')
def left_iv_btn(context):
    time.sleep(1)
    left_iv_btn = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/left_iv_btn")')
    left_iv_btn.click()


@given(u'登录测试_点击退出登录')
def tv_title_1(context):
    time.sleep(1)
    tv_title = context.driver.find_element_by_android_uiautomator('new UiSelector().text("退出登录")')
    tv_title.click()


@given(u'登录测试_点击退出登录_1')
def logout(context):
    time.sleep(1)
    utils.utils_button1(context)
