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

    def __init__(self, api_key):
        self.api_key = api_key
        self.request = FMRequest()
        self.request.set_api_key(self.api_key)
        self.customer_api = CustomerApi(api_key, self.request)
        self.customers = list()
        self.enable_full_description = False
        self.id=None
        self.company = None
        self.email=None
        self.allow_ach=None
        self.created_at=None
        self.updated_at=None

    def use_demo(self):
        self.request.use_env("demo")
        self.customer_api.request.use_env("demo")

    def __repr__(self):
        if self.enable_full_description:
            return """
                "merchant_id": {mid},
                "company": {company} ,
                "email": {email} ,
                "name": {name} ,
                "ach allowed?": {allow_ach} ,
                "created at": {created_at} ,
                """.format(
                mid=self.id,
                company=self.company,
                email=self.email,
                name=self.name,
                allow_ach=self.allow_ach,
                created_at=self.created_at
            )
        else:
            return """
                "merchant_id": {mid},
                "company": {company} ,
                """.format(
                company=self.company if self.company is not None else "Not set",
                mid=self.id,
            )

    def update_merchant_info(self):
        """
        Call fattmerchant api and gets all the merchant info
        """
        endpoint = "self"
        response = json.loads(self.request.get_request(endpoint))
        try:
            logger.debug(response)
            merchant_info = response['merchant']
            self.company = merchant_info['company_name']
            self.id = merchant_info['id']
            self.email = merchant_info['contact_email']
            self.name = response['user']['name']
            self.allow_ach = merchant_info['allow_ach']
            self.created_at = merchant_info['created_at']
            self.updated_at = merchant_info['updated_at']
            self.enable_full_description = True
        except:
            self.company = None
            self.name = None
            self.enable_full_description = False
            logger.error(
                "unable to set/find merchant info.. is api key correct ?")

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
        Get all the customers for the merchant
    :return: list of all customers
    :rtype: list()
        """
        endpoint = "customer"
        answer = json.loads(self.request.get_request(endpoint))
        self.customers = [] if self.customers is None else self.customers
        try:
            for customer in answer["data"]:
                next_customer = Customer(customer, self.id)
                next_customer.payment_methods = self.customer_api.payment_methods(next_customer.id)
                self.customers.append(next_customer)
            return self.customers
        except Exception as e:
            logger.error("exeption happend {}".format(e))
            return None

    def charge_customer_tokenized(self, customer_id):
        charge_to_customer = None
        for customer in self.customers:
            if customer_id == customer.id:
                charge_to_customer = customer
        if charge_to_customer is None:
            logger.error("unable to find customer for the merchant")
            return False
        else:
            charge_to_customer

    def add_customer(self, customer: Customer):
        """
        Add a new customer for a merchant object
        """
        endpoint = "customer"
        body = customer.to_json()
        answer = json.loads(self.request.post_request(endpoint, body=body))
        logger.info(answer)
        return answer

    def get_all_invoices(self):
        """
        Gets all the invoices to customer by a merchant
        """
        endpoint = "invoice"
        answer = self.request.get_request(endpoint)
        return answer

    def get_items_by_code(self):
        """
        Gets a particular item specified by the code
        """
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
