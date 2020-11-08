#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/7 23:53
# @Author  : dreamlane
# @File    : main.py
from selenium.webdriver.common.by import By
from web_selenium_2.page.add_user import AddUser
from web_selenium_2.page.basepage import BasePage
from web_selenium_2.page.import_users import ImportUsers


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # 点击添加成员
    def add_user(self):
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddUser(self.driver)

    # 点击导入通讯录
    def import_users(self):
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        return ImportUsers(self.driver)
