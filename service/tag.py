#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project: hogwarts_lg4
# @File    : tag.py
# @Author  : xianyu
# @Time    : 2020-12-03 15:49:53
import json

import requests

corpid = 'ww4beb383165e58b35'
corpsecret = '8P-VljcSUw47l2eTREvdOlAU_vN9JMVyWloBIA4r62Q'


class Tag:
    def __init__(self):
        self.token = ''

    # 获取token
    def gettoken(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={'corpid': corpid, 'corpsecret': corpsecret}
        )
        if r.json()['errcode'] == 0:
            self.token = r.json()['access_token']
        else:
            return r.json()

    # 获取企业标签库
    def get_corp_tag_list(self, tag_id: list = None):
        if self.token == '':
            self.gettoken()
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={'access_token': self.token},
            json={'tag_id': tag_id}
        )
        print(json.dumps(r.json(), indent=2))
        return r

    # 添加企业客户标签
    def add_crop_tag(self, group_name, tag_names, group_id=None, order=None):
        if self.token == '':
            self.gettoken()
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={'access_token': self.token},
            json={
                'group_id': group_id,
                'group_name': group_name,
                'order': order,
                'tag': tag_names
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r

    # 编辑企业客户标签
    def edit_corp_tag(self, tag_id, name=None, order=None):
        if self.token == '':
            self.gettoken()
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            params={'access_token': self.token},
            json={
                'id': tag_id,
                'name': name,
                'order': order
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r

    # 删除企业客户标签
    def del_corp_tag(self, **id):
        """
        :param id: tag_id 和 group_id 不能同时为空
        :return:
        """
        if self.token == '':
            self.gettoken()
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={'access_token': self.token},
            json=id
        )
        print(json.dumps(r.json(), indent=2))
        return r
