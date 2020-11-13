#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 23:20
# @Author  : dreamlane
# @File    : add_cl5.py

# 手动输入添加页面
import yaml
from appium.webdriver.common.mobileby import MobileBy

from app_appium_1.page.basepage import BasePage


class AddCl5(BasePage):
    def submit_msg(self):
        with open("../page/add_cl5.yaml", encoding='utf-8') as f:
            dic = yaml.safe_load(f)[0]
            self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(
                dic["name"])
            self.driver.find_element(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
            if dic["gender"] == "男":
                self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
            else:
                self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

            self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(dic["phonenum"])
            self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']").click()
            result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
            return result
