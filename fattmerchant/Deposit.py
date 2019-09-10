# -*- coding: utf-8 -*-
from __future__ import absolute_import

import json
import logging

from .FattmerchantException import InvalidRequestDataException

__author__ = "austin.burns@fattmerchant.com"
logger = logging.getLogger(__name__)


class Deposit():
    """
    Class to allow interfacing with deposits within the Fattmerchant API
    """
    def __init__(self, api_key, request):
        self.api_key = api_key
        self.request = request
        self.api = "fq"

    def list(self, options):
        """
        Gets a list of deposits within a certain fate range from the API
        """

        if ("startDate" not in options and "endDate" not in options):
            msg = "At least a startDate or endDate" \
                " is required to make this request."

            raise InvalidRequestDataException(msg)

        endpoint = "deposit"
        response = json.loads(self.request.get(self.api, endpoint, options))

        return response['data']

    def get(self, options):
        """
        Gets a batch deposit's details within a certain date range from the API
        """

        if ("startDate" not in options):
            msg = "A startDate is required to perform this request."

            raise InvalidRequestDataException(msg)

        endpoint = "depositDetail"
        response = json.loads(self.request.get(self.api, endpoint, options))

        return response['data']
