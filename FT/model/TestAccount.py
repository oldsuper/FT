#!/usr/bin/env python
# coding=utf-8
"""
@Author  : gaosongbo
@Contact : gaosongbo@knowin.com
@File    : TestAccount.py
@Time    : 2020/3/2 2:35 下午
"""


class TestAccount:
    def __init__(self, **kwargs):
        self.accountToken = kwargs['accountToken']
        self.accountId = kwargs['accountId']
