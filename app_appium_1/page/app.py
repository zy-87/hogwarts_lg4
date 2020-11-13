#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 21:43
# @Author  : dreamlane
# @File    : app.py

"""消息主界面"""
from appium import webdriver
from app_appium_1.page.address_book import AddressBook
from app_appium_1.page.basepage import BasePage


class App(BasePage):
    def start(self):
        package = "com.tencent.wework"
        activity = "com.tencent.wework.launch.WwMainActivity"
        if self.driver is None:
            caps = {}
            caps['platformName'] = 'android'
            caps['deviceName'] = 'hogwarts'
            caps['appPackage'] = package
            caps['appActivity'] = activity
            caps['autoGrantPermissions'] = True     # 自动授权
            caps['noReset'] = 'true'  # 避免每次启动对app初始化.避免同意弹窗
            caps['dontStopAppOnReset'] = 'true'
            caps['skipDeviceInitialization'] = 'true'
            caps['unicodeKeyBoard'] = 'true'  # 输入英文以外的文字时需要设置
            caps['resetKeyBoard'] = 'true'
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(3)
        else:
            self.driver.start_activity(package, activity)  # 启动app
        return self

    def main(self):
        self.steps("../page/main.yaml")
        return AddressBook(self.driver)     # 通讯录
