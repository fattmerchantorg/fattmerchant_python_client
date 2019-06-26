# -*- coding: utf-8 -*-
"""

For defining fattmerchant merhcant class
"""

from .Customer import CustomerApi
from .FMRequestHelper import FMRequest
import logging

__author__ = "tanmay.datta86@gmail.com"
logger = logging.getLogger(__name__)


class Merchant:
    """
    Class to maintain merchant object easily

    """

    def __init__(self, api_key, company=None, name=None):
        self.api_key = api_key
        self.request = FMRequest()
        #self.request.set_api_key(self.api_key)
        self.name = name if name is not None else None
        self.company = company
        self.customers = CustomerApi(api_key, self.request,
                                     self.company)
        self.id = None

    def __repr__(self):
        return """
            "merchant_id": {mid},
            "company": {company} ,
            """.format(
            company=self.company if self.company is not None else "Not set",
            mid=self.id,
        )

    def create(self, name=None):
        """
        Can be used to create merchant if the api key is good
        """
        if self.name is None and name is None:
            return "Merchant name should be provided, call as .create(<name>)"
        else:
            if name is not None:
                self.name = name
        endpoint = "merchant/get_info"
        body = {
            "name": self.name,
            "company": self.company,
            "api_key": self.api_key
        }
        id_info = self.request.put_request(endpoint, body=body)
        # set id here
        return self.id

    def items(self):
        """
        Shows all the items that merchant has in store. 
        """
        endpoint = "items"
        self.request.get_request(endpoint)

    def get_items_by_code(self):
        endpoint = "item/code"
        self.request.get_request(endpoint)

    def set_merchant_id(self, id):
        """
        Sets the merchant id, Required in case we are getting
        merchant info from some other source and want to use
        fattmerchant client to interact with api 
        """
        self.id = id
