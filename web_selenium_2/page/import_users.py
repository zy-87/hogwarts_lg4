#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/8 0:06
# @Author  : dreamlane
# @File    : import_users.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web_selenium_2.page.add_user import AddUser
from web_selenium_2.page.basepage import BasePage


class ImportUsers(BasePage):
    # 导入通讯录
    def import_users(self, filepath):
        # 点击 上传文件. 上传文件应选中input标签后使用send_keys
        self.find(By.XPATH, "//*[@id='main']/div/div[2]/div[2]/div[1]/a/input").send_keys(
            filepath)
        # 显式等待确保添加成功
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
            By.XPATH, "//*[@id='main']/div/div[2]/div[2]/div[1]/div[2]"
        ))
        # 点击导入
        self.find(By.CSS_SELECTOR, ".ww_fileImporter_submitWrap a").click()
        # 显式等待确保导入成功
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            By.CSS_SELECTOR, ".ww_fileImporter_successBtnWrap a"
        ))
        # 点击完成跳转到添加成员
        self.find(By.CSS_SELECTOR, ".ww_fileImporter_successBtnWrap a").click()
        return AddUser(self.driver)