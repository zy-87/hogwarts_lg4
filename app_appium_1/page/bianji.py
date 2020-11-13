#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 23:49
# @Author  : dreamlane
# @File    : bianji.py
from app_appium_1.page.basepage import BasePage
from app_appium_1.page.delpage import DelPage


class BianJi(BasePage):
    def goto_delpage(self):
        self.steps("../page/bianji.yaml")
        return DelPage(self.driver)