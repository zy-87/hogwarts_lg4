#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/7 23:44
# @Author  : dreamlane
# @File    : basepage.py
import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ''

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            # option = Options()
            # option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver
        if self._base_url != '':
            self.driver.get(self._base_url)

            # # 此代码用来手动登录获取并将cookie写入文件
            # sleep(30)
            # cookies = self.driver.get_cookies()
            # with open("cookie", 'w') as f:
            #     f.write(json.dumps(cookies))

            with open('cookie', 'r') as f:
                cookies = json.loads(f.read())
                for cookie in cookies:
                    if 'expiry' in cookie:
                        del cookie['expiry']
                    self.driver.add_cookie(cookie)
            self.driver.refresh()  # 刷新登录状态

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)
