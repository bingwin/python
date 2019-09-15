# -*- coding: utf-8 -*-

from behave import *
import time
import utils


@given(u'好友_搜索好友')
def tv_friend_search(context):
    time.sleep(1)
    tv_friend_search = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/tv_friend_search")')
    time.sleep(1)
    tv_friend_search.click()


@given(u'好友_获取手机号控件')
def search_bar_text(context):
    time.sleep(1)
    search_bar_text = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/search_bar_text")')
    time.sleep(1)
    search_bar_text.click()


# @given(u'登录测试_输入手机号:"{phone}"')
@given(u'好友_输入119202:"{number}"')
def input(context, number):
    time.sleep(0.5)
    search_bar_text = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/search_bar_text")')
    search_bar_text.set_value(str(number))


@given(u'好友_点击搜索框')
def user_search_recommend_text(context):
    time.sleep(1)
    user_search_recommend_text = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/user_search_recommend_text")')
    time.sleep(1)
    user_search_recommend_text.click()


@given(u'好友_发送消息')
def tv_friend_relation(context):
    time.sleep(1)
    tv_friend_relation = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/tv_friend_relation")')
    time.sleep(1)
    tv_friend_relation.click()


@given(u'好友_输入框:"{message}"')
def input_edit(context, message):
    time.sleep(1)
    input_edit = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/input_edit")')
    time.sleep(1)
    input_edit.click()
    time.sleep(1)
    input_edit.set_value(str(message))


@given(u'好友_发送')
def send_btn(context):
    time.sleep(0.5)
    send_btn = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/send_btn")')
    send_btn.click()


# @given(u'好友_语音')
# def audio_record_btn(context):
#     time.sleep(0.5)
#     audio_record_btn = context.driver.find_element_by_android_uiautomator(
#         'new UiSelector().resourceId("com.kwai.sogame:id/audio_record_btn")')
#     audio_record_btn.click()
#
#
# @given(u'好友_长按语音')
# def audio_iv(context):
#     time.sleep(0.5)
#     audio_iv = context.driver.find_element_by_android_uiautomator(
#         'new UiSelector().resourceId("com.kwai.sogame:id/audio_iv")')
#     audio_iv.long_click(duration=3, timeout=3)


@given(u'好友_游戏邀请')
def game_btn(context):
    time.sleep(0.5)
    game_btn = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/game_btn")')
    game_btn.click()


@given(u'好友_斗兽棋邀请')
def game_invite(context):
    time.sleep(0.5)
    # context.driver.tap()
    game_invite = context.driver.find_element_by_android_uiautomator('new UiSelector().text("斗兽棋")')
    game_invite.click()


@given(u'好友_发送照片')
def photo_album_btn(context):
    time.sleep(0.5)
    photo_album_btn = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/photo_album_btn")')
    photo_album_btn.click()

@given(u'好友_点击第一张图片')
def photo_1(context):
    time.sleep(1)
    photo_1 = context.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/"
        "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
        "android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
        "android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.ImageView")
    photo_1.click()

@given(u'好友_选中照片')
def checkbox(context):
    time.sleep(2)
    checkbox = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/checkbox")')
    checkbox.click()

@given(u'好友_发送_2')
def send_btn(context):
    time.sleep(0.5)
    send_btn = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/send_btn")')
    send_btn.click()

@given(u'好友_点击emoji')
def smiley_btn(context):
    time.sleep(1)
    smiley_btn = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/smiley_btn")')
    smiley_btn.click()

@given(u'好友_发送emoji')
def emoji_view(context):
    time.sleep(1)
    emoji_view = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/emoji_view")')
    emoji_view.click()

@given(u'好友_发送_3')
def send_btn(context):
    time.sleep(0.5)
    send_btn = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/send_btn")')
    send_btn.click()

@given(u'好友_返回')
def send_btn(context):
    time.sleep(0.5)
    left_iv_btn = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/left_iv_btn")')
    left_iv_btn.click()

@given(u'好友_返回_2')
def send_btn(context):
    time.sleep(0.5)
    left_iv_btn = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/left_iv_btn")')
    left_iv_btn.click()

@given(u'好友_取消')
def send_btn(context):
    time.sleep(0.5)
    search_bar_cancel = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.kwai.sogame:id/search_bar_cancel")')
    search_bar_cancel.click()

@given(u'好友_返回_3')
def send_btn(context):
    time.sleep(2)
    left_iv_btn = context.driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
        'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
        'android.widget.RelativeLayout[1]/android.widget.ImageView')
    left_iv_btn.click()


# /hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.ImageView


# com.kwai.sogame:id/left_iv_btn

# com.kwai.sogame:id/left_iv_btn

# com.kwai.sogame:id/search_bar_cancel

# com.kwai.sogame:id/left_iv_btn

# 设置


# com.kwai.sogame:id/checkbox 勾选框

# com.kwai.sogame:id/send_btn 发送框

# com.kwai.sogame:id/smiley_btn emoji

# com.kwai.sogame:id/emoji_view     点击第一个emoji图发送   看是否能发送成功


# /hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.ImageView


# @given(u'好友_emoji')
# def smiley_btn(context):
#     time.sleep(0.5)
#     smiley_btn = context.driver.find_element_by_android_uiautomator(
#         'new UiSelector().resourceId("com.kwai.sogame:id/smiley_btn")')
#     smiley_btn.click()


# 如果我们执行behave —tags=slow,slow1 只要被tag为slow或slow1的scenario被执行

# user_search_recommend_text
# @


# 输入框 input_edit
# 发送 send_btn
# 语音 audio_record_btn   audio_iv
# 游戏邀请 game_btn
# 照片 photo_album_btn
# emoji smiley_btn
