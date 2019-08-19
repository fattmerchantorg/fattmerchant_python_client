# -*- coding: utf-8 -*-
"""
For defining helper classes for fattmerchant merchant behaviour
"""

from __future__ import absolute_import

import json
import logging

from .Customer import Customer

__author__ = "tanmay.datta86@gmail.com"
logger = logging.getLogger(__name__)


class MerchantItems(object):
    """
    Helper Class for creating merchant items
    """
    def __init__(self, itemJson):
        self.id = itemJson["id"]
        self.user_id = itemJson["user_id"]
        self.merchant_id = itemJson["merchant_id"]


class Merchant():
    """
    Class to maintain merchant object easily

    """
    def __init__(self, api_key, request, customer):
        self.api_key = api_key
        self.request = request

    def __repr__(self):
        if self.enable_full_description:
            return """
                "merchant_id": {mid},
                "company": {company} ,
                "email": {email} ,
                "name": {name} ,
                "ach allowed?": {allow_ach} ,
                "created at": {created_at} ,
                """.format(mid=self.id,
                           company=self.company,
                           email=self.email,
                           name=self.name,
                           allow_ach=self.allow_ach,
                           created_at=self.created_at)
        else:
            return """
                "merchant_id": {mid},
                "company": {company} ,
                """.format(company=self.company
                           if self.company is not None else "Not set",
                           mid=self.id)

    def update_merchant_info(self, name=None):
        """
        Call fattmerchant api and gets all the merchant info
        """
        endpoint = "merchant/?company_name={}".format(name)
        response = json.loads(self.request.get(endpoint=endpoint))

        try:
            logger.debug(response)
            merchant_info = response[u'data'][0]
            self.company = merchant_info[u'company_name']
            self.id = merchant_info[u'id']
            self.email = merchant_info[u'contact_email']
            self.name = response[u'user'][u'name']
            self.allow_ach = merchant_info[u'allow_ach']
            self.created_at = merchant_info[u'created_at']
            self.updated_at = merchant_info[u'updated_at']
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
        if name is None:
            return "Merchant name should be provided, call as .create(<name>)"

        endpoint = "merchant"
        body = {
            "name": self.name,
            "company": self.company,
            "api_key": self.api_key
        }
        id_info = self.request.put(endpoint=endpoint, payload=body)
        logger.debug("id info is {}".format(id_info))
        # set id here
        return self.id

    def items(self):
        """
        Shows all the items that merchant has in store. 
        """
        endpoint = "item"
        answer = json.loads(self.request.get(endpoint=endpoint))
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
        answer = json.loads(self.request.get(endpoint=endpoint))
        self.customers = [] if self.customers is None else self.customers
        try:
            for customer in answer["data"]:
                next_customer = Customer(customer, self.id)
                next_customer.payment_methods = self.customer.payment_methods(
                    next_customer.id)
                self.customers.append(next_customer)
            return self.customers
        except Exception, e:
            logger.error("exeption happend {}".format(e))
            return None

    def charge_customer_on_token(self, customer_id, token_id, data):
        """

        Works exactly like charge  customer tokenized function but 
        do not check for the existence of customer and needs a token id

        :return: answer from the fattmerchant API
        :rtype: dict()

        """
        endpoint = "charge"
        # todo: check if the customer exiss

        payment_method_id = token_id
        logger.info("id returned by call =====> {}".format(payment_method_id))
        body = {
            "payment_method_id": payment_method_id,
            "meta": data["meta"],
            "total": data["total"],
            "pre_auth": data["pre_auth"]
        }
        answer = self.request.post(endpoint=endpoint, payload=body)
        logger.debug(json.loads(answer))
        return json.loads(answer)

    def charge_customer_tokenized(self, customer_id, data):
        """

        Charge a customer for merchant. 
        ***requires a data dictionary with following mandatory keys***
        - meta
        - total and
        - pre_auth

        the example structure for meta is 

        .. code-block:: python

            "meta": {
                "tax":2,
                "subtotal":10
                "lineItems": [{
                    "id": "optional-fm-catalog-item-id"
                    "item":"Demo Item",
                    "details":"this is a regular demo item",
                    "quantity":10,
                    "price": .1
                    }]
                },

        .. note::

            "total" is the amount you need to charge the customer

        :return: answer from the fattmerchant API
        :rtype: dict()

        """
        charge_to_customer = None
        endpoint = "charge"
        self.get_all_customers()
        logger.debug(self.customers)
        for customer in self.customers:
            if customer_id == customer.id:
                charge_to_customer = customer
        if charge_to_customer is None:
            logger.error("unable to find customer for the merchant")
            return False
        else:
            payment_method_id = charge_to_customer.payment_methods[0][u'id']
            logger.info(
                "id returned by call =====> {}".format(payment_method_id))
            body = {
                "payment_method_id": payment_method_id,
                "meta": data["meta"],
                "total": data["total"],
                "pre_auth": data["pre_auth"]
            }
            answer = self.request.post(endpoint=endpoint, payload=body)
            logger.debug(json.loads(answer))
            return json.loads(answer)

    def add_customer(self, customer):
        """

        Add a new customer for a merchant object

        :return: answer from the fattmerchant API
        :rtype: dict()

        """
        endpoint = "customer"
        body = customer.to_json()
        answer = json.loads(self.request.post(endpoint=endpoint, payload=body))
        logger.info(answer)
        return answer

    def get_all_invoices(self):
        """
        Gets all the invoices to customer by a merchant

        :return: all invoices from the fattmerchant API
        :rtype: dict()

        """
        endpoint = "invoice"
        answer = json.loads(self.request.get(endpoint=endpoint))
        return answer

    def get_items_by_code(self):
        """

        Gets a particular item specified by the code

        """
        endpoint = "item/code"
        return json.loads(self.request.get(endpoint=endpoint))

    def set_merchant_id(self, id):
        """

        .. warning::
            Anti pattern here but just it is here to make sure
            we can test the library.

        Sets the merchant id, Required in case we are getting
        merchant info from some other source and want to use
        fattmerchant client to interact with api 
        """
        self.id = id
