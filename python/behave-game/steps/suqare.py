# -*- coding: utf-8 -*-

from behave import *
import time
import utils

@given(u'广场_点赞')
def like(context):
    time.sleep(2)
    dianzan = context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/tv_like")')
    time.sleep(1)
    dianzan.click()

@given(u'广场_更多')
def square_more(context):
    utils.utils_square_more(context)

@given(u'广场_关注')
def square_more_1(context):
    utils.utils_square_more_1(context)

@given(u'广场_举报')
def square_more_2(context):
    utils.utils_square_more_2(context)

@given(u'广场_选择举报理由')
def select_reason(context):
    time.sleep(1)
    select_reason =context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/rb_ads")')
    # select_reason = context.driver.find_element_by_id("com.kwai.sogame:id/rb_ads")
    select_reason.click()

@given(u'广场_提交举报')
def tv_submit(context):
    time.sleep(1)
    tv_submit =context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/tv_submit")')
    # tv_submit = context.driver.find_element_by_id('com.kwai.sogame:id/tv_submit')
    tv_submit.click()

@given(u'广场_发布按钮')
def right_btn(context):
    time.sleep(1)
    right_btn =context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/right_btn")')
    # right_btn = context.driver.find_element_by_id('com.kwai.sogame:id/right_btn')
    right_btn.click()

@given(u'广场_输入文字:"{test}"')
def edit_publish_content(context,test):
    time.sleep(1)
    edit_publish_content_1 = context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/edit_publish_content")')
    # edit_publish_content_1 = context.driver.find_element_by_id('com.kwai.sogame:id/edit_publish_content')
    edit_publish_content_1.click()
    edit_publish_content_1.set_value(str(test))

@given(u'广场_点击发布')
def txt_publish_publish(context):
    time.sleep(1)
    txt_publish_publish = context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/txt_publish_publish")')
    # txt_publish_publish = context.driver.find_element_by_id('com.kwai.sogame:id/txt_publish_publish')
    txt_publish_publish.click()

@given(u'广场_删除')
def text1(context):
    time.sleep(1)
    text2 = context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/text1")')
    # text2 = context.driver.find_element_by_id('com.kwai.sogame:id/text1')
    text2.click()

@given(u'广场_确认删除')
def txt_publish_publish(context):
    time.sleep(1)
    button1 = context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/button1")')
    # button1 = context.driver.find_element_by_id('com.kwai.sogame:id/button1')
    button1.click()



