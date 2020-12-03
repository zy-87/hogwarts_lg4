#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project: hogwarts_lg4
# @File    : test_tag.py
# @Author  : xianyu
# @Time    : 2020-12-03 15:50:11
import json

import pytest

from service.tag import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag()
        self.id = {  # 收集测试中添加的标签id
            "tag_id": [],
            "group_id": []
        }

    def teardown_class(self):
        print(self.id)
        self.tag.del_corp_tag(**self.id)  # 脏数据清理

    # 测试获取企业标签库  获取所有标签组, 获取指定的单个/多个标签组, 获取不存在的标签组
    @pytest.mark.parametrize("tag_id", [
        [],  # 获取所有标签列表
        ['et8PVGCwAAzOVONzSMrHPiAMuZEKn6RQ'],  # 获取单个指定标签列表
        ['et8PVGCwAApPvMzyD05Qxt1Xv3Uvj-lQ', 'et8PVGCwAAN90CZElDC4_W9-be-Z4mQg'],  # 获取多个指定标签列表
        ['xxxxxxxx']  # 获取不存在的标签列表
    ])
    def test_get_crop_tag_list(self, tag_id):
        r = self.tag.get_corp_tag_list(tag_id)
        try:
            assert r.json()['errcode'] == 0
        except Exception as e:
            print(f"{tag_id}不存在")

    # 测试添加企业客户标签  et8PVGCwAAXjEr618N44pHUPTodQ0Mhw
    @pytest.mark.parametrize("group_name, tag_names, group_id, order", [
        ['test02', [{'name': 'tag01'}, {'name': 'tag02'}], None, None],  # 添加多个标签
        ['测试三组', [{'name': '#^*&%$(#'}], None, None],  # 特殊符号命名
        ['测试四组', [{'name': '不重要'}], 'et8PVGCwAAXjEr618N44pHUPTodQ0Mhw', 3],  # 指定标签组添加标签
        ['测试四组', [{'name': '不重要'}], 'et8PVGCwAAXjEr618N44pHUPTodQ0Mhw', 3],  # 重复添加
        ['超长名字超长名字超长名字超长名字超长名字超长名字超长名字超长', [{'name': '#^*&%$(#'}], None, None],
        ['测试三组', [{'name': '超长名字超长名字超长名字超长名字超长名字超长名字超长名字超长'}], None, None],
        ['超出限制超出限制超出限制超出限制超出限制超出限制超出限制超出限制', [{'name': '#^*&%$(#'}], None, None],
        ['测试三组', [{'name': '超出限制超出限制超出限制超出限制超出限制超出限制超出限制超出限制'}], None, None],
    ])
    def test_add_crop_tag(self, group_name, tag_names, group_id, order):
        r = self.tag.add_crop_tag(group_name, tag_names, group_id, order)
        # 添加请求返回的标签组名和标签名列表
        add_crop_tag_group_name = r.json()['tag_group']['group_name']
        add_crop_tag_tag_names = [name['name'] for name in r.json()['tag_group']['tag']]
        # 添加请求返回的标签组id和标签id
        add_crop_tag_group_id = r.json()['tag_group']['group_id']
        add_crop_tag_tag_ids = [name['id'] for name in r.json()['tag_group']['tag']]
        # 将id加入收集信息中
        self.id['group_id'].append(add_crop_tag_group_id)
        for name in add_crop_tag_tag_ids:
            self.id['tag_id'].append(name)
        # 重新请求获取标签列表
        r = self.tag.get_corp_tag_list()
        get_corp_tag_list_group_names = [group['group_name'] for group in r.json()['tag_group']]
        get_corp_tag_list_tag_names = [tag['name'] for group in r.json()['tag_group'] for tag in group['tag']]
        assert add_crop_tag_group_name in get_corp_tag_list_group_names
        for name in add_crop_tag_tag_names:
            assert name in get_corp_tag_list_tag_names

    # 测试编辑企业客户标签
    @pytest.mark.parametrize("tag_id, name, order", [
        ['et8PVGCwAAXjEr618N44pHUPTodQ0Mhw', None, None],  # 标签组id
        ['et8PVGCwAAzOVONzSMrHPiAMuZEKn6RQ', None, None],  # 标签id
        ['et8PVGCwAAXjEr618N44pHUPTodQ0Mhw', '标签组改名测试', None],
        ['et8PVGCwAAzOVONzSMrHPiAMuZEKn6RQ', '标签改名测试', None],
        ['et8PVGCwAAXjEr618N44pHUPTodQ0Mhw', '标签组改名测试', -99],  # 排序
        ['et8PVGCwAAzOVONzSMrHPiAMuZEKn6RQ', '超长名字超长名字超长名字超长名字超长名字超长名字超长名字超长', None],
        ['et8PVGCwAAzOVONzSMrHPiAMuZEKn6RQ', '@#$%^&&*(()(*&*^%$', None],
        ['et8PVGCwAAzOVONzSMrHPiAMuZEKn6RQ', '超出限制超出限制超出限制超出限制超出限制超出限制超出限制超出限制', None],
    ])
    def test_edit_corp_tag(self, tag_id, name, order):
        self.tag.edit_corp_tag(tag_id, name, order)
        r = self.tag.get_corp_tag_list()
        get_corp_tag_list_group_names = [group['group_name'] for group in r.json()['tag_group']]
        get_corp_tag_list_tag_names = [tag['name'] for group in r.json()['tag_group'] for tag in group['tag']]
        assert name in get_corp_tag_list_group_names or name in get_corp_tag_list_tag_names

    # 测试删除企业客户标签
    @pytest.mark.parametrize("id", [
        {},
        {'tag_id': ['et8PVGCwAAzOVONzSMrHPiAMuZEKn6RQ']},  # 删除单个标签
        {'tag_id': ['et8PVGCwAAzOVONzSMrHPiAMuZEKn6RQ', 'et8PVGCwAA3Bj2gH1uNj51WMKCaL9q_w']},  # 删除多个标签
        {'group_id': ['et8PVGCwAAXjEr618N44pHUPTodQ0Mhw']},  # 删除单个标签组
        {'group_id': ['et8PVGCwAAXjEr618N44pHUPTodQ0Mhw', 'et8PVGCwAA7hSN2dC_Jtdd2qY5mRVkaQ']},  # 删除多个标签组
        {'tag_id': ['et8PVGCwAA3Bj2gH1uNj51WMKCaL9q_w']}, {'group_id': ['et8PVGCwAA7hSN2dC_Jtdd2qY5mRVkaQ']},
        {'tag_id': ['et8PVGCwAAzOVONzSMrHPiAMuZEKn6RQ']},  # 删除不存在的
    ])
    def test_del_corp_tag(self, id):
        print(id)
        if len(id.items()) == 0:
            print("tag_id 和 group_id 不可同时为空")
        else:
            r = self.tag.del_corp_tag(**id)
            assert r.json()['errcode'] == 0
