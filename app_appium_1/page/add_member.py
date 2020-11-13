#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 22:30
# @Author  : dreamlane
# @File    : add_member.py
from app_appium_1.page.add_cl5 import AddCl5
from app_appium_1.page.basepage import BasePage


class AddMember(BasePage):
    def add_func(self):
        self.steps("../page/add_member.yaml")
        return AddCl5(self.driver)