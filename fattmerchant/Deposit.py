# -*- coding: utf-8 -*-
from __future__ import absolute_import

import json
import logging

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
            msg = "At least startDate or endDate \
                   are required to make this request"

            raise AttributeError(msg)

        endpoint = "deposit"
        response = json.loads(self.request.get(self.api, endpoint, options))

        try:
            logger.debug(response)

            return json.dumps(response['data'])
        except AttributeError:
            logger.error(
                "Unable to make request with options: {}".format(options))

    def get(self, options):
        """
        Gets a batch deposit's details within a certain date range from the API
        """

        if ("startDate" not in options):
            msg = "A startDate is required to perform this request"

            raise AttributeError(msg)

        endpoint = "depositDetail"
        response = json.loads(self.request.get(self.api, endpoint, options))

        try:
            logger.debug(response)

            return json.dumps(response['data'])
        except AttributeError:
            logger.error("The deposit id that was passed in is invalid")
