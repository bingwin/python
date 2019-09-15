# -*- coding: utf-8 -*-

from behave import *
import time
import utils


@given(u'广场_聊天')
def utils_tab3(context):
    time.sleep(1)
    tab3 = context.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/"
                                                "android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/"
                                                "android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/"
                                                "android.widget.RelativeLayout[3]/android.widget.ImageView[1]")
    tab3.click()


@given(u'广场_广场')
def utils_tab2(context):
    time.sleep(1)
    tab2 = context.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/"
                                                "android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/"
                                                "android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/"
                                                "android.widget.RelativeLayout[2]/android.widget.ImageView[1]")
    tab2.click()
    tab2.click()


@given(u'广场_点赞')
def iv_feed_like(context):
    time.sleep(2)
    iv_feed_like = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/iv_feed_like")')
    time.sleep(1)
    iv_feed_like.click()


@given(u'广场_更多')
def square_more(context):
    time.sleep(1)
    square_more = context.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.kwai.sogame:id/iv_operation")')
    square_more.click()

@given(u'广场_关注')
def square_more_1(context):
    time.sleep(1)
    square_more_1 = context.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/"
        "android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.TextView[1]")
    square_more_1.click()

@given(u'广场_举报')
def square_more_2(context):
    time.sleep(1)
    square_more_2 = context.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/"
        "android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.TextView[2]")
    square_more_2.click()

@given(u'广场_选择举报理由')
def select_reason(context):
    time.sleep(1)
    select_reason = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/rb_ads")')
    # select_reason = context.driver.find_element_by_id("com.kwai.sogame:id/rb_ads")
    time.sleep(1)
    select_reason.click()


@given(u'广场_提交举报')
def tv_submit(context):
    time.sleep(1)
    tv_submit = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/tv_submit")')
    # tv_submit = context.driver.find_element_by_id('com.kwai.sogame:id/tv_submit')
    time.sleep(1)
    tv_submit.click()


@given(u'广场_发布按钮')
def right_btn(context):
    time.sleep(1)
    right_btn = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/right_btn")')
    # right_btn = context.driver.find_element_by_id('com.kwai.sogame:id/right_btn')
    time.sleep(1)
    right_btn.click()


@given(u'广场_输入文字:"{test}"')
def edit_publish_content(context, test):
    time.sleep(1)
    edit_publish_content_1 = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/edit_publish_content")')
    # edit_publish_content_1 = context.driver.find_element_by_id('com.kwai.sogame:id/edit_publish_content')
    edit_publish_content_1.click()
    time.sleep(1)
    edit_publish_content_1.set_value(str(test))


@given(u'广场_点击发布')
def txt_publish_publish(context):
    time.sleep(1)
    txt_publish_publish = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/txt_publish_publish")')
    # txt_publish_publish = context.driver.find_element_by_id('com.kwai.sogame:id/txt_publish_publish')
    time.sleep(1)
    txt_publish_publish.click()


@given(u'广场_删除')
def text1(context):
    time.sleep(1)
    text2 = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/text1")')
    # text2 = context.driver.find_element_by_id('com.kwai.sogame:id/text1')
    text2.click()


@given(u'广场_确认删除')
def txt_publish_publish(context):
    time.sleep(1)
    button1 = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/button1")')
    # button1 = context.driver.find_element_by_id('com.kwai.sogame:id/button1')
    button1.click()

# /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[2]
