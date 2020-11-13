#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 23:11
# @Author  : dreamlane
# @File    : personal_information.py
from app_appium_1.page.basepage import BasePage
from app_appium_1.page.bianji import BianJi


class PersonalInformation(BasePage):
    def goto_bianji(self):
        self.steps("../page/personal_information.yaml")
        return BianJi(self.driver)