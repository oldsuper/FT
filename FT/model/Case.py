#!/usr/bin/env python
# coding=utf-8
"""
@Author  : gaosongbo
@Contact : gaosongbo@knowin.com
@File    : Case.py
@Time    : 2020/3/2 11:49 上午
"""

from FT.utils.FtRequests import *

class Case:
    def __init__(self, caseId, caseName, stepIdList, level, allStep,
                 ready=0, useFor=0, domain=None, *args, **kwargs):
        """

        :param caseId:
        :param caseName:
        :param stepIdList:
        :param level: filter
        :param ready: 0 ok, 1 no
        :param useFor: 0 both, 1 cloud, 2 offline
        :param domain: filter
        :param args:
        :param kwargs:
        """
        self.caseId = caseId
        self.caseName = caseName
        self.level = level
        self.ready = ready
        self.useFor = useFor
        self.domain = domain
        self.steps = []
        for stepId in stepIdList:
            self.steps.append(allStep[stepId])

    def sendRequest(self):
        for step in self.steps:
            sendRequest()
