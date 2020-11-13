#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 23:52
# @Author  : dreamlane
# @File    : delpage.py
from appium.webdriver.common.mobileby import MobileBy

from app_appium_1.page.basepage import BasePage


class DelPage(BasePage):
    def del_person(self):
        name = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').text
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("删除成员").instance(0));').click()
        self.driver.find_element(MobileBy.ID, "bit").click()
        return name

