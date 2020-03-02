#!/usr/bin/env python
# coding=utf-8
"""
@Author  : gaosongbo
@Contact : gaosongbo@knowin.com
@File    : Environment.py
@Time    : 2020/3/2 11:52 上午
"""
from FT.model.TestAccount import TestAccount
import yaml
import os


class Environment:
    # @property
    # def host(self):
    #     return self.host
    #
    # @property
    # def port(self):
    #     return self.port
    #
    # @host.setter
    # def host(self, host):
    #     if isinstance(host, str):
    #         self.host = host
    #     else:
    #         raise TypeError
    #
    # @port.setter
    # def port(self, port):
    #     if isinstance(port, (int, str)):
    #         self.host = port
    #     else:
    #         raise TypeError

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError

    @property
    def envDomain(self):
        return self.envDomain

    @envDomain.setter
    def envDomain(self, envDomain):
        if isinstance(envDomain, str):
            self.envDomain = envDomain
        else:
            raise TypeError

    @property
    def defaultTestAccount(self):
        return self.defaultTestAccount

    @defaultTestAccount.setter
    def defaultTestAccount(self, defaultTestAccount):
        if isinstance(defaultTestAccount, TestAccount):
            self.defaultTestAccount = defaultTestAccount
        else:
            raise TypeError

    def __init__(self, name, envData):
        self.name(name)
        self.envDomain(envData['envDomain'])
        self.defaultTestAccount(TestAccount(envData['token'], envData['id']))


class Environments:
    def __init__(self, configYmlFile):
        """
        :param configYmlFile:
        """
        if os.path.exists(configYmlFile):
            self.environments = {}
            configData = yaml.load(file(configYmlFile))
            for name in configData:
                self.environments[name] = Environment(name, configData[name])
        else:
            raise ValueError(configYmlFile)

    def getTestEnv(self, environmentName):
        if self.environments.__contains__(environmentName):
            return self.environments[environmentName]
