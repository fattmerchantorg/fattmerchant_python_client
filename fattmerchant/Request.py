# -*- coding: utf-8 -*-
"""

This module cotains helper functions/class for creating fattmerchant requests
    :copyright: 2019 Fattmerchant
    :license: MIT
    :author: Tanmay Dutta

"""

from __future__ import with_statement
from __future__ import absolute_import
import requests
import os
import json
import logging

self_path = os.path.dirname(__file__)
logger = logging.getLogger(__name__)


class Request():
    """

    Class to get a valid fattmerchant request format

    """
    def __init__(self, api_key, env):
        self.api_key = api_key
        self.use_env(env)

    def use_env(self, env):
        """
        change enviornment for testing

        :param env: string of enviornment can be "demo", "mock" or "prod"

        """

        prod_url = 'https://apiprod.fattlabs.com'
        demo_url = 'https://apidemo.fattlabs.com'
        local_url = 'http://localhost:8000'
        mock_url = 'https://private-anon-c4e1c18d13-fattmerchant.apiary-mock.com/'

        self.env = env

        if (env == "demo"):
            self.api_url = demo_url
        elif (env == "mock"):
            self.api_url = mock_url
        elif (env == "local"):
            self.api_url = local_url
        elif (env == "prod"):
            self.api_url = prod_url

    def build_request(self, endpoint):
        url = ("{api_url}/{endpoint}").format(api_url=self.api_url,
                                              endpoint=endpoint)
        headers = self.build_headers()

        return url, headers

    def build_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {api_key}'.format(api_key=self.api_key),
            'Accept': 'application/json'
        }

    def get_request(self, endpoint):
        """

        To call all the "get" request with a given endpoint
        for information on what endpoints are valid/available go to 
        https://fattmerchant.com/api-documentation/

        :param str endpoint: string for fattmerchant API endpoint

        """
        url, headers = self.build_request(endpoint)

        logger.error("ERROR occured while trying send a GET request: \
                      URL: {}, HEADERS: {}".format(url, headers))

        req = requests.get(url, headers=headers)

        if req.status_code == 200:
            return req.text
        else:
            logger.error("ERROR occured while trying send a GET request: \
                          URL: {}, HEADERS: {}, \
                          STATUS CODE: {}, RESPONSE: {}".format(
                url, headers, req.status_code, req.text))

            return req.text

    def put_request(self, endpoint, body=None):
        """

        To call all the "put" request with a given endpoint
        for information on what endpoints are valid/available go to 
        https://fattmerchant.com/api-documentation/


        :param str endpoint: string for fattmerchant API endpoint

        """
        url, headers = self.build_request(endpoint)

        req = requests.put(url, headers=headers, data=json.dumps(body))

        if req.status_code == 200:
            return req.text
        else:
            logger.error("ERROR occured while trying send a GET request: \
                          URL: {}, HEADERS: {}, \
                          STATUS CODE: {}, RESPONSE: {}".format(
                url, headers, req.status_code, req.text))

            return req.text

    def post_request(self, endpoint, body=None):
        """

        To call all the "post" request with a given endpoint
        for information on what endpoints are valid/available go to 
        https://fattmerchant.com/api-documentation/

        :param str endpoint: string for fattmerchant API endpoint

        """
        url, headers = self.build_request(endpoint)

        req = requests.post(url, headers=headers, data=json.dumps(body))

        if req.status_code == 200:
            return req.text
        else:
            logger.error("ERROR occured while trying send a GET request: \
                          URL: {}, HEADERS: {}, \
                          STATUS CODE: {}, RESPONSE: {}".format(
                url, headers, req.status_code, req.text))

            return req.text
