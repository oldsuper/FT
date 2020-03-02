#!/usr/bin/env python
# coding=utf-8
"""
@Author  : gaosongbo
@Contact : gaosongbo@knowin.com
@File    : FtRequests.py.py
@Time    : 2020/3/2 11:29 上午
@Desc    :
"""
import requests


def sendRequest(url, params, method='post', headers=None, *args, **kwargs):
    """

    :param url:
    :param headers:
    :param params:
    :param method:
    :param args:
    :param kwargs:
    """
    if method == 'post':
        return requests.post(url, params=params, headers=headers)
    elif method == 'get':
        return requests.get(url, params=params, headers=headers)
    return requests.request(method, url, params)
