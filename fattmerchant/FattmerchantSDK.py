# -*- coding: utf-8 -*-
"""
For defining helper classes for fattmerchant merchant behaviour
"""

from __future__ import absolute_import

from .Request import Request

from .Customer import CustomerApi
from .Merchant import Merchant
from .Team import Team
from .Transaction import Transaction
from .Deposit import Deposit


class FattmerchantSDK(object):
    """
    Class to set up the Fattmerchant Python SDK

    """
    def __init__(self, api_key, env="prod"):
        self.api_key = api_key
        self.request = Request(api_key, env)
        self.customer = CustomerApi(api_key, self.request)
        self.merchant = Merchant(api_key, self.request, self.customer)
        self.team = Team(api_key, self.request)
        self.transaction = Transaction(api_key, self.request)
        self.deposit = Deposit(api_key, self.request)
