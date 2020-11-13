#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 0:07
# @Author  : dreamlane
# @File    : test_case.py
import pytest
import yaml

from app_appium_1.page.app import App


class TestCase:
    driver = App()
    """
    通过 address_book.yaml 控制 添加 或是 删除, 删除可直接指定要删除的人名
    通过 add_cl5.yaml 指定要添加的成员信息
    """
    @pytest.mark.skip
    def test_add(self):
        result = self.driver.start().main().goto_add_member().add_func().submit_msg()
        assert result == "添加成功"

    def test_del(self):
        result = self.driver.start().main().goto_add_member().goto_bianji().goto_delpage().del_person()
        with open("../page/address_book.yaml", encoding='utf-8') as f:
            name = yaml.safe_load(f)[0]["text"]
            assert result == name