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
        ["毛台", 2, 12345678912],
        ["蘑菇头", 3, 13568914759],
    ])
    def test_add_user(self, name, account, phone):
        self.main.add_user().input_message(name, account, phone)
        assert name in self.main.add_user().get_users()

    def test_import_users(self, filepath):
        namelist = self.main.import_users().import_users(filepath).get_users()
        with open(filepath, 'r') as f:
            for name in namelist:
                assert name in f.read()


if __name__ == '__main__':
    pytest.main()
