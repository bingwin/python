# -*- coding: utf-8 -*-

from behave import *
import time

# 侧边栏相机按钮 com.smile.gifmaker:id/right_btn
# 一键开启 com.smile.gifmaker:id/grant_record_all_permission_btn
# 始终允许 com.android.packageinstaller:id/permission_allow_button
# 始终允许 com.android.packageinstaller:id/permission_allow_button

# 拍11秒 com.smile.gifmaker:id/record_btn_bg
# 下一步 com.smile.gifmaker:id/editor_sdk_player






@given(u'点击相机按钮')
def right_btn(context):
    time.sleep(2)
    right_btn = context.driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.smile.gifmaker:id/right_btn")')
    right_btn.click()




