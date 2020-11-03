#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 0:37
# @Author  : dreamlane
# @File    : test_cookie.py
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWorkWechat:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_work_wechat(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        """
        此代码用来手动登录获取并将cookie写入文件
        sleep(30)
        cookies = self.driver.get_cookies()
        with open("cookie", 'w') as f:
            f.write(json.dumps(cookies))
        """
        with open('cookie', 'r') as f:
            cookies = json.loads(f.read())
            for cookie in cookies:
                if 'expiry' in cookie:
                    del cookie['expirty']
                self.driver.add_cookie(cookie)
        self.driver.refresh()  # 刷新登录状态
        # 点击 导入通讯录
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 点击 上传文件. 上传文件应选中input标签后使用send_keys
        self.driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/div[1]/a/input").send_keys(
            "./村办国际无限公司通讯录.xlsx")
        # 获取上传后的文件名
        filename = self.driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/div[1]/div[2]").text
        assert "村办国际无限公司通讯录" in filename
        sleep(5)
