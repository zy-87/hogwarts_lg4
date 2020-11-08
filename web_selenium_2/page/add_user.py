#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/8 0:06
# @Author  : dreamlane
# @File    : add_user.py
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web_selenium_2.page.basepage import BasePage


class AddUser(BasePage):
    # 输入姓名,账号,手机号后点击保存
    def input_message(self, name, account, phone):
        self.find(By.ID, "username").send_keys(name)  # 输入姓名
        self.find(By.ID, "memberAdd_acctid").click()  # 获取焦点
        self.find(By.ID, "memberAdd_acctid").send_keys(account)  # 输入账号
        self.find(By.ID, "memberAdd_phone").send_keys(phone)  # 输入电话

        self.finds(By.CSS_SELECTOR, ".js_btn_save")[0].click()  # 点击保存后判断是否成功
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located(self.find(By.ID, "party_name")))
            return True  # 保存成功返回True,否则返回False
        except Exception:
            return False

    # 获取通讯录成员姓名列表
    def get_users(self):
        ele_list = self.finds(By.XPATH, '//*[@id="member_list"]/tr/td[2]')
        name_list = []
        for ele in ele_list:
            name_list.append(ele.get_attribute("title"))
        return name_list
