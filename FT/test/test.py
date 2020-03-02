#!/usr/bin/env python
# coding=utf-8
"""
@Author  : gaosongbo
@Contact : gaosongbo@knowin.com
@File    : test.py
@Time    : 2020/3/2 2:57 下午
"""


def a(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)


if __name__ == '__main__':
    a({'a': 111}, b=11)
