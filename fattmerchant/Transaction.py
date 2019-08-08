# -*- coding: utf-8 -*-
from __future__ import absolute_import

import json
import logging

__author__ = "tanmay.datta86@gmail.com"
logger = logging.getLogger(__name__)


class Transaction():
    """
    Class to allow interfacing with transactions within the Fattmerchant API
    """
    def __init__(self, api_key, request):
        self.api_key = api_key
        self.request = request

    def list(self, page=None):
        """
        Gets a list of transactions from the API
        """

        endpoint = "transaction" if not page \
            else "transaction/?page={}".format(page)
        response = json.loads(self.request.get_request(endpoint))

        logger.debug(response)
        data = response['data']

        return json.dumps(data)

    def get(self, id):
        """
        Gets a single transaction's details from the API
        """

        endpoint = "transaction/{}".format(id)
        response = json.loads(self.request.get_request(endpoint))

        try:
            logger.debug(response)

            return json.dumps(response)
        except EnvironmentError:
            logger.error("The transaction id that was passed in is invalid")

    def refund(self, id, amount):
        """
        Refund a certain amount of a transaction
        """

        endpoint = "transaction/{}/refund".format(id)
        response = json.loads(
            self.request.post_request(endpoint, dict(total=amount)))

        try:
            logger.debug(response)

            return json.dumps(response)
        except EnvironmentError:
            logger.error("The transaction id that was passed in is invalid")
