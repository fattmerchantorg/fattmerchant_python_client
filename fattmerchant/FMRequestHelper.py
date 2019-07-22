# -*- coding: utf-8 -*-
"""

This module cotains helper functions/class for creating fattmerchant requests
    :copyright: 2019 Fattmerchant
    :license: MIT
    :author: Tanmay Dutta

"""

import requests
import os
import json
import logging

self_path = os.path.dirname(__file__)
logger = logging.getLogger(__name__)

class FMRequest():
    """

    Class to get a valid fattmerchant request format

    """
    fm_link_prod = r'https://apiprod.fattlabs.com'
    fm_demo_link = r'https://apidemo.fattlabs.com/'
    fm_mock_link = r'https://private-anon-c4e1c18d13-fattmerchant.apiary-mock.com/'
    fm_link = fm_link_prod
    try:
        with open(os.path.join(self_path,"test_api_key.txt"), 'r') as api_file:
            api_key_default = api_file.read()
    except:
        logger.debug("test api key not found")
    def __init__(self):
        self.header = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {api_key}',
                       'Accept': 'application/json'}
        self.body = None
        self.api_key = FMRequest.api_key_default

    def use_env(self, env:str):
        """
        change enviornment for testing

        :param env: string of enviornment can be "demo", "mock" or "prod"

        """

        if(env == "demo"):
            logger.debug("using demo account")
            self.fm_link = self.fm_demo_link
        elif (env == "mock"):
            self.fm_link = self.fm_mock_link
        else:
            self.fm_link = self.fm_link_prod
            
            
    def get_request(self, endpoint: str, body:dict=None):
        """

        To call all the "get" request with a given endpoint
        for information on what endpoints are valid/available go to 
        https://fattmerchant.com/api-documentation/

        :param str endpoint: string for fattmerchant API endpoint

        """
        url = self.fm_link + "/" + endpoint
        logger.debug("trying =====> {}".format(url))
        self.body = body
        self.api_key = self.api_key_default if self.api_key is None else self.api_key
        self.update_header()
        logger.debug("trying =====> header = {}".format(self.header))
        if self.body is not None:
            req = requests.get(url, headers=self.header, data=self.body)
        else:
            req = requests.get(url, headers=self.header)
        logger.debug("request got req = {}".format(req))
        logger.debug("request answer = {}".format(req.content))
        return req.text
    
    def put_request(self, endpoint: str, body=None):
        """

        To call all the "put" request with a given endpoint
        for information on what endpoints are valid/available go to 
        https://fattmerchant.com/api-documentation/


        :param str endpoint: string for fattmerchant API endpoint

        """
        url = self.fm_link + "/" + endpoint
        self.body = body
        self.api_key = self.api_key_default if self.api_key is None else self.api_key
        self.update_header()
        if self.body is not None:
            req = requests.put(url, headers=self.header, data=self.body)
        else:
            req = requests.put(url, headers=self.header)
        return req.text

    def post_request(self, endpoint: str, body=None):
        """

        To call all the "post" request with a given endpoint
        for information on what endpoints are valid/available go to 
        https://fattmerchant.com/api-documentation/

        :param str endpoint: string for fattmerchant API endpoint

        """
        url = self.fm_link + "/" + endpoint
        self.body = body
        self.api_key = self.api_key_default if self.api_key is None else self.api_key
        self.update_header()
        logger.info("body ==> {}".format(json.dumps(self.body)))
        if self.body is not None:
            req = requests.post(url, headers=self.header, data=json.dumps(self.body))
        else:
            req = requests.post(url, headers=self.header)
        if req.status_code == 200:
            return req.text
        else:
            logger.error("request error ===> status code: {}".format(req.status_code))
            logger.error("Error while post ==> {}, body ==> {}".format(url, body))
            logger.error("response got ===> {}".format(req.text))
            return None

    def set_api_key(self, key:str):
        """

        To set the API key that is provided by the fattmerchant support

        """
        self.api_key = key
    
    def update_header(self):
        """

        Internal helper function

        """
        self.header['Authorization'] = self.header['Authorization'].format(api_key = self.api_key)


