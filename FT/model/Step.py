#!/usr/bin/env python
# coding=utf-8
"""
@Author  : gaosongbo
@Contact : gaosongbo@knowin.com
@File    : Step.py
@Time    : 2020/3/2 11:49 上午
"""
import types


class StepEnv:
    @property
    def envDomain(self):
        return self.envDomain

    @property
    def account(self):
        return self.account

    @envDomain.setter
    def envDomain(self, envDomain):
        if isinstance(envDomain, str):
            self.envDomain = envDomain
        else:
            raise TypeError

    @account.setter
    def account(self, account):
        if isinstance(account, ):
            self.envDomain = account
        else:
            raise TypeError

class StepRequest:
    @property
    def extra(self):
        return self.extra

    @property
    def query(self):
        return self.query

    @extra.setter
    def extra(self, extra):
        if isinstance(extra, (types.Dict, None)):
            self.extra = extra
        else:
            raise TypeError('Extra must be DICT')

    @query.setter
    def query(self, query):
        if isinstance(query, str):
            self.query = query
        else:
            self.query = str(query)

    def __init__(self, query, extra=None):
        self.extra(extra)
        self.query(query)


class StepAsserts:
    def __init__(self):
        return


class StepAssert:
    @property
    def responseValueXpath(self):
        return self.responseValueXpath

    @responseValueXpath.setter
    def responseValueXpath(self, responseValueXpath):
        if isinstance(responseValueXpath, str):
            if responseValueXpath.startswith('$.') or responseValueXpath.startswith('.'):
                self.responseValueXpath = responseValueXpath
            else:
                raise ValueError("responseValueXpath must startswith '.' or '$.'")
        else:
            raise TypeError("responseValueXpath must be STR")

    @property
    def assertFunction(self):
        return self.assertFunction

    @assertFunction.setter
    def assertFunction(self, assertFunction):
        if isinstance(assertFunction, str):
            self.assertFunction = assertFunction
        else:
            raise TypeError

    @property
    def expectValue(self):
        return self.expectValue

    @expectValue.setter
    def expectValue(self, expectValue):
        self.expectValue = expectValue

    def __init__(self, responseValueXpath, assertFunction, expectValue):
        self.responseValueXpath(responseValueXpath)
        self.assertFunction(assertFunction)
        self.expectValue(expectValue)


class Step:
    stepAsserts = []
    _responseValueXpaths = []

    @property
    def stepRequest(self):
        return self.stepRequest

    @stepRequest.setter
    def stepRequest(self, stepRequest):
        if isinstance(stepRequest, StepAssert):
            self.stepRequest = stepRequest
        else:
            raise TypeError

    @property
    def StepAsserts(self):
        return self.stepRequests

    @StepAsserts.setter
    def StepAsserts(self, stepRequests):
        if isinstance(stepRequests, (types.Tuple, list)):
            # xpath重复的跳过
            if self._responseValueXpaths.count(stepRequests.responseValueXpath) == 0:
                for stepRequest in stepRequests:
                    self.stepRequests.append(stepRequest)
        else:
            raise TypeError
