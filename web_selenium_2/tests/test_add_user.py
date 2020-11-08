#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/8 17:03
# @Author  : dreamlane
# @File    : test_add_user.py
from time import sleep

import pytest

from web_selenium_2.page.main import Main


class TestAddUser:
    filepath = "../../web_selenium_1/村办国际无限公司通讯录.xlsx"

    def setup(self):
        self.main = Main()
        self.main.driver.implicitly_wait(5)
        self.main.driver.maximize_window()

    def teardown(self):
        sleep(5)
        self.main.driver.quit()

    @pytest.mark.parametrize(['name', 'account', 'phone'], [
        ["毛台", 2, 12345678912]
    ])
    def test_add_user(self, name, account, phone):
        add_user_page = self.main.add_user()
        add_user_page.input_message(name, account, phone)
        assert name in add_user_page.get_users()

    def test_import_users(self, filepath):
        self.main.import_users().import_users(filepath).get_users()


if __name__ == '__main__':
    pytest.main()
