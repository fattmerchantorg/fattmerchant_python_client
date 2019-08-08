# -*- coding: utf-8 -*-
u"""

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
from io import open

self_path = os.path.dirname(__file__)
logger = logging.getLogger(__name__)


class FMRequest(object):
    u"""

    Class to get a valid fattmerchant request format

    """
    fm_link_prod = ur'https://apiprod.fattlabs.com'
    fm_demo_link = ur'https://apidemo.fattlabs.com/'
    fm_mock_link = ur'https://private-anon-c4e1c18d13-fattmerchant.apiary-mock.com/'
    fm_link = fm_link_prod

    def __init__(self):
        self.header = {
            u'Content-Type': u'application/json',
            u'Authorization': u'Bearer {api_key}',
            u'Accept': u'application/json'
        }
        self.body = None

    def use_env(self, env):
        u"""
        change enviornment for testing

        :param env: string of enviornment can be "demo", "mock" or "prod"

        """

        if (env == u"demo"):
            logger.debug(u"using demo account")
            self.fm_link = self.fm_demo_link
        elif (env == u"mock"):
            self.fm_link = self.fm_mock_link
        else:
            self.fm_link = self.fm_link_prod

    def get_request(self, endpoint, body=None):
        u"""

        To call all the "get" request with a given endpoint
        for information on what endpoints are valid/available go to 
        https://fattmerchant.com/api-documentation/

        :param str endpoint: string for fattmerchant API endpoint

        """
        url = self.fm_link + u"/" + endpoint
        logger.debug(u"trying =====> {}".format(url))
        self.body = body
        self.api_key = self.api_key_default if self.api_key is None else self.api_key
        self.update_header()
        logger.debug(u"trying =====> header = {}".format(self.header))
        if self.body is not None:
            req = requests.get(url, headers=self.header, data=self.body)
        else:
            req = requests.get(url, headers=self.header)
        logger.debug(u"request got req = {}".format(req))
        logger.debug(u"request answer = {}".format(req.content))
        return req.text

    def put_request(self, endpoint, body=None):
        u"""

        To call all the "put" request with a given endpoint
        for information on what endpoints are valid/available go to 
        https://fattmerchant.com/api-documentation/


        :param str endpoint: string for fattmerchant API endpoint

        """
        url = self.fm_link + u"/" + endpoint
        self.body = body
        self.api_key = self.api_key_default if self.api_key is None else self.api_key
        self.update_header()
        if self.body is not None:
            req = requests.put(url, headers=self.header, data=self.body)
        else:
            req = requests.put(url, headers=self.header)
        return req.text

    def post_request(self, endpoint, body=None):
        u"""

        To call all the "post" request with a given endpoint
        for information on what endpoints are valid/available go to 
        https://fattmerchant.com/api-documentation/

        :param str endpoint: string for fattmerchant API endpoint

        """
        url = self.fm_link + u"/" + endpoint
        self.body = body
        self.api_key = self.api_key_default if self.api_key is None else self.api_key
        self.update_header()
        logger.info(u"body ==> {}".format(json.dumps(self.body)))
        if self.body is not None:
            req = requests.post(url,
                                headers=self.header,
                                data=json.dumps(self.body))
        else:
            req = requests.post(url, headers=self.header)
        if req.status_code == 200:
            return req.text
        else:
            logger.error(u"request error ===> status code: {}".format(
                req.status_code))
            logger.error(u"Error while post ==> {}, body ==> {}".format(
                url, body))
            logger.error(u"response got ===> {}".format(req.text))
            return req.text

    def set_api_key(self, key):
        u"""

        To set the API key that is provided by the fattmerchant support

        """
        self.api_key = key

    def update_header(self):
        u"""

        Internal helper function

        """
        self.header[u'Authorization'] = self.header[u'Authorization'].format(
            api_key=self.api_key)
        
        
