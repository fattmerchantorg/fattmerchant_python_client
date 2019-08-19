# -*- coding: utf-8 -*-
"""

This module cotains helper functions/class for creating fattmerchant requests
    :copyright: 2019 Fattmerchant
    :license: MIT
    :author: Austin Burns

"""

from __future__ import with_statement
from __future__ import absolute_import
import requests
import os
import logging
import json

self_path = os.path.dirname(__file__)
logger = logging.getLogger(__name__)


class Request():
    """

    Class to get a valid fattmerchant request format

    """
    def __init__(self, api_key, env="prod"):
        self.api_key = api_key
        self.use_env(env)

    def use_env(self, env):
        """
        change enviornment for testing

        :param env: string of enviornment can be "demo", "mock" or "prod"

        """

        prod_url = 'https://apiprod.fattlabs.com'
        prod_fq_url = 'https://apiprod.fattlabs.com/query'
        demo_url = 'https://apidemo.fattlabs.com'
        demo_fq_url = 'https://apidemo.fattlabs.com/query'
        local_url = 'http://localhost:8000'
        local_fq_url = 'http://localhost:3005'
        mock_url = 'https://private-anon-c4e1c18d13-fattmerchant.apiary-mock.com'
        mock_fq_url = 'http://localhost:8000'

        self.env = env
        self.api = {}

        if (env == "prod"):
            self.api["core"] = prod_url
            self.api["fq"] = prod_fq_url
        elif (env == "demo"):
            self.api["core"] = demo_url
            self.api["fq"] = demo_fq_url
        elif (env == "local"):
            self.api["core"] = local_url
            self.api["fq"] = local_fq_url
        elif (env == "mock"):
            self.api["core"] = mock_url
            self.api["fq"] = mock_fq_url

    def __make_request(self,
                       api_type,
                       method,
                       endpoint,
                       options={},
                       payload=None):
        url = "{api}/{endpoint}{query_string}".format(
            api=self.api[api_type],
            endpoint=endpoint,
            query_string=self.__build_query_string(options))

        headers = self.__build_headers()

        # Get the correct "requests" class method by passing
        # in the request method that we want
        req = getattr(requests, method, 'get')

        if payload is not None:
            res = req(url, headers=headers, data=json.dumps(payload))
        else:
            res = req(url, headers=headers)

        if res.status_code == 200:
            return res.text
        else:
            logger.error("ERROR occured while trying to send a {} request: \
                            URL: {}, HEADERS: {}, PAYLOAD: {} \
                            STATUS CODE: {}, RESPONSE: {}".format(
                method.upper(), url, headers, payload, res.status_code,
                res.text))

            return res.text

    def __build_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {api_key}'.format(api_key=self.api_key),
            'Accept': 'application/json'
        }

    def __build_query_string(self, params):
        if (len(params) == 0):
            return ""

        query_strings = []

        for key, value in params.items():
            query_strings.append("{}={}".format(key, value))

        return "?{}".format("&".join(query_strings))

    def get(self, api='core', endpoint='', options={}):
        """
        Calls respective api with a `GET` HTTP method

        :param str api: Fattmerchant API base url to be requested
        :param str endpoint: API endpoint to be requested
        """
        return self.__make_request(api, 'get', endpoint, options=options)

    def post(self, api='core', endpoint='', payload={}):
        """
        Calls respective api with a `POST` HTTP method

        :param str api: Fattmerchant API base url to be requested
        :param str endpoint: API endpoint to be requested
        :param dict payload: Data to be sent along with API request
        """
        return self.__make_request(api, 'post', endpoint, payload=payload)

    def put(self, api='core', endpoint='', payload={}):
        """
        Calls respective api with a `PUT` HTTP method

        :param str api: Fattmerchant API base url to be requested
        :param str endpoint: API endpoint to be requested
        :param dict payload: Data to be sent along with API request
        """
        return self.__make_request(api, 'put', endpoint, payload=payload)
