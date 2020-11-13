#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 20:56
# @Author  : dreamlane
# @File    : basepage.py
import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    blacks = []
    params = {}

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 查找元素
    def find(self, by, locator=None):
        try:
            ele = self.driver.find_element(*by) if isinstance(by, tuple) else self.driver.find_element(by, locator)
            return ele
        except Exception as e:
            # 处理因弹窗导致的找不到元素
            for black in self.blacks:  # 如果弹窗在黑名单,能正确处理;不在,不走if,for循环结束抛出错误
                eles = self.driver.find_elements(*black)
                if len(eles) > 0:
                    eles[0].click()
                    return self.find(self, by, locator)
            raise e

    # send方法
    def send(self, value, by, locator):
        try:
            self.find(by, locator).send_keys(value)
        except Exception as e:
            # 处理因弹窗导致的无法输入
            for black in self.blacks:  # 如果弹窗在黑名单,能正确处理;不在,不走if,for循环结束抛出错误
                eles = self.driver.find_elements(*black)
                if len(eles) > 0:
                    eles[0].click()
                    return self.send(self, value, by, locator)
            raise e

    # 其他操作
    def steps(self, path):
        with open(path, encoding='utf-8') as f:
            steps: list[dict] = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    ele = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    if "click" == step["action"]:
                        ele.click()
                    if "send" == step["action"]:
                        value: str = step["value"]
                        # value使用python定义的值
                        for param in self.params:    # 默认循环的是字典的keys列表
                            value = value.replace(f"{param}", self.params[param])
                        self.send(value, step["by"], step["locator"])
