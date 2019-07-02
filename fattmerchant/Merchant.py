# -*- coding: utf-8 -*-
"""

For defining fattmerchant merhcant class
"""

from .Customer import CustomerApi, Customer
from .FMRequestHelper import FMRequest
import json
import logging

__author__ = "tanmay.datta86@gmail.com"
logger = logging.getLogger(__name__)

class MerchantItems:
    """
    Helper Class for creating merchant items
    """
    def __init__(self, itemJson):
        self.id = itemJson["id"]
        self.user_id = itemJson["user_id"]
        self.merchant_id = itemJson["merchant_id"]

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
        self.customer_api = CustomerApi(api_key, self.request,
                                     self.company)
        self.customers = list()
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
        endpoint = "item"
        answer = json.loads(self.request.get_request(endpoint))
        logger.debug(answer)
        items = answer["data"]
        self.merchant_items = []
        for item in items:
            logger.debug(item)
            self.merchant_items.append(MerchantItems(item))
        return self.merchant_items

    def get_all_customers(self):
        """
        get all the customers for the merchant
        """
        endpoint = "customer"
        answer = json.loads(self.request.get_request(endpoint))
        self.customer = [] if self.customers is None else self.customers
        for customer in answer["data"]:
            self.customers.append(Customer(customer, self.id))
        logger.debug(self.customers[0])
        return self.customers


    def get_all_invoices(self):
        """
        Gets all the invoices to customer by a merchant
        """
        endpoint = "invoice"
        answer = self.request.get_request(endpoint)
        return answer

    def get_items_by_code(self):
        endpoint = "item/code"
        return self.request.get_request(endpoint)


    def set_merchant_id(self, id):
        """
        ***Anti pattern here but just it is here to make sure
        we can test the library.***

        Sets the merchant id, Required in case we are getting
        merchant info from some other source and want to use
        fattmerchant client to interact with api 
        """
        self.id = id
