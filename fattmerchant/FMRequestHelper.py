"""
This module cotains helper functions/class for creating fattmerchant requests
"""

import requests
import os
import json
import logging

self_path = os.path.dirname(__file__)
logger = logging.getLogger(__name__)

class FMRequest():
    "Class to get a valid fattmerchant request format"
    fm_link_prod = r'https://apiprod.fattlabs.com'
    fm_demo_link = r'https://apidemo.fattlabs.com/'
    fm_mock_link = r'https://private-anon-c4e1c18d13-fattmerchant.apiary-mock.com/'
    fm_link = fm_link_prod
    with open(os.path.join(self_path,"test_api_key.txt"), 'r') as api_file:
        api_key_default = api_file.read()
    def __init__(self):
        self.header = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {api_key}',
                       'Accept': 'application/json'}
        self.body = None
        self.api_key = FMRequest.api_key_default

    def use_env(self, env):
        """
        change enviornment for testing
        """

        if(env == "demo"):
            logger.debug("using demo account")
            self.fm_link = self.fm_demo_link
        elif (env == "mock"):
            self.fm_link = self.fm_mock_link
        else:
            self.fm_link = self.fm_link_prod
            
            
    def get_request(self, endpoint: str, body=None):
        """
        To call all the "get" request with a given endpoint
        for information on what endpoints are valid/available go to 
        https://fattmerchant.com/api-documentation/
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
        """
        url = self.fm_link + "/" + endpoint
        self.body = body
        self.api_key = self.api_key_default if self.api_key is None else self.api_key
        self.update_header()
        logger.info("body ==> {}".format(self.body))
        if self.body is not None:
            req = requests.post(url, headers=self.header, data=json.dumps(self.body))
        else:
            req = requests.post(url, headers=self.header)
        return req.text

    def set_api_key(self, key):
        """
        To set the API key that is provided by the fattmerchant support
        """
        self.api_key = key
    
    def update_header(self):
        """
        Internal helper function
        """
        self.header['Authorization'] = self.header['Authorization'].format(api_key = self.api_key)


