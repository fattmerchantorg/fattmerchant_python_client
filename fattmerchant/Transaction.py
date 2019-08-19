# -*- coding: utf-8 -*-
from __future__ import absolute_import

import json
import logging

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

        logger.debug(response)

        return response["data"]

    def get(self, id):
        """
        Gets a single transaction's details from the API
        """

        endpoint = "transaction/{}".format(id)
        response = json.loads(self.request.get(endpoint=endpoint))

        try:
            logger.debug(response)

            return response
        except EnvironmentError:
            logger.error("The transaction id that was passed in is invalid")

    def refund(self, id, amount):
        """
        Refund a certain amount of a transaction
        """

        endpoint = "transaction/{}/refund".format(id)
        payload = {"total": amount}
        response = json.loads(
            self.request.post(endpoint=endpoint, payload=payload))

        try:
            logger.debug(response)

            return response
        except EnvironmentError:
            logger.error("The transaction id that was passed in is invalid")
