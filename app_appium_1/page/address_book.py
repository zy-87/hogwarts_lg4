#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 22:00
# @Author  : dreamlane
# @File    : address_book.py
"""通讯录界面"""
import yaml
from appium.webdriver.common.mobileby import MobileBy

from app_appium_1.page.add_member import AddMember
from app_appium_1.page.basepage import BasePage
from app_appium_1.page.personal_information import PersonalInformation


class AddressBook(BasePage):
    def goto_add_member(self):
        with open("../page/address_book.yaml", encoding='utf-8') as f:
            dic = yaml.safe_load(f)[0]
            if dic["text"] == "添加成员":
                self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                         'new UiScrollable(new UiSelector()'
                                         '.scrollable(true).instance(0))'
                                         '.scrollIntoView(new UiSelector()'
                                         f'.text("{dic["text"]}").instance(0));').click()
                return AddMember(self.driver)  # 添加成员页面
            else:
                try:
                    self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                             'new UiScrollable(new UiSelector()'
                                             '.scrollable(true).instance(0))'
                                             '.scrollIntoView(new UiSelector()'
                                             f'.text("{dic["text"]}").instance(0));').click()
                    return PersonalInformation(self.driver)     # 个人信息界面
                except Exception as e:
                    print(f"成员 : {dic['text']} 不在通讯录中")
                    raise e
