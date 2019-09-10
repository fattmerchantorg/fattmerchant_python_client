# -*- coding: utf-8 -*-
from __future__ import absolute_import

import json
import logging

from .FattmerchantException import InvalidRequestDataException

__author__ = "austin.burns@fattmerchant.com"
logger = logging.getLogger(__name__)


class Transaction():
    """
    Class to allow interfacing with transactions within the Fattmerchant API
    """
    def __init__(self, api_key, request):
        self.api_key = api_key
        self.request = request

    def list(self, options={}):
        """
        Gets a list of transactions from the API
        """

        endpoint = "transaction"
        response = json.loads(
            self.request.get(endpoint=endpoint, options=options))

        return response["data"]

    def get(self, id=None):
        """
        Gets a single transaction's details from the API
        """

        if not isinstance(id, str) or id is None:
            msg = "An id of type string has to be passed in with the request."

            raise InvalidRequestDataException(msg)

        endpoint = "transaction/{}".format(id)

        return json.loads(self.request.get(endpoint=endpoint))

    def refund(self, id=None, amount=None):
        """
        Refund a certain amount of a transaction
        """

        if not isinstance(id, str) or id is None:
            msg = "An id of type string has to be passed in with the request."

            raise InvalidRequestDataException(msg)

        if not isinstance(amount, float) \
                or isinstance(amount, int) or amount is None:
            msg = "An amount of type int or float has to be passed " \
                "in with the request."

            raise InvalidRequestDataException(msg)

        endpoint = "transaction/{}/refund".format(id)
        payload = {"total": amount}

        return json.loads(self.request.post(endpoint=endpoint,
                                            payload=payload))
