# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time
import os

img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/Uiautomator2/screenshots/'   #截图保持路径

d = u2.connect_usb('6e48b8db')

d.app_start("com.smile.gifmaker")

time.sleep(2)

d(resourceId="com.smile.gifmaker:id/left_btn").click()

time.sleep(1)

d(resourceId="com.smile.gifmaker:id/tv_game_center").click()

def test_1(i):

    time.sleep(1)

    d(text="推荐").click()

    time.sleep(1)

    d(text="魔力转圈圈").click()

    time.sleep(1)

    print(img_folder)

    os.chdir(img_folder)

    s = str(i)

    d.screenshot(s+"home.png")

    d(resourceId="com.smile.gifmaker:id/left_btn").click()

for i in range(0, 1):
    test_1(i)

# d.

# d(resourceId="com.kwai.sogame:id/phone_tv").click()

# import re
#
# r = re.compile(r"new\ UiSelector\(\)\.(\w+)\(\"(.*)\"")
# print((r.match('new UiSelector().resourceId("com.kwai.game.doll:id/image_tourit"').group(1)))
