from __future__ import absolute_import
__author__ = u"tanmay.datta86@gmail.com"

import logging
import json

logger = logging.getLogger(__name__)


class CustomersController(object):
    """
    Helper class for getting customer related information.
    """
    def __init__(self, api_key, request=None, company=None):
        self.api_key = api_key
        self.request = request
        self.company = company

    def __repr__(self):
        return u"""
            "for_company": {company} ,
            "merchant_id": {mid},
            """.format(company=self.company if self.company else u"None", )

    @staticmethod
    def all_customers():
        u""" Return a collection of all customers. """
        pass

    def create(self, params):
        u"""
        Create a Customer
        No field is required

        .. code-block:: python

            example: = fattmerchant.Customer.create({
                "company": "Some company",
                "first_name": "John"
            })
        
        An example of creating an customer with all available fields

        .. code-block:: JSON
        
            {
                "firstname": "John",
                "lastname": "Smith",
                "company": "ABC INC",
                "email": "demo@fattmerchant.com",
                "cc_emails": ["daniel@fattmerchant.com"],
                "phone": "1234567898",
                "address_1": "123 Rite Way",
                "address_2": "Unit 12",
                "address_city": "Orlando",
                "address_state": "FL",
                "address_zip": "32801",
                "address_country": "USA",
                "reference": "BARTLE"
            }

        """

        logging.debug(u"creating customer")

        endpoint = u'customer'
        body = {
            u"firstname": params.get(u"first_name", u""),
            u"lastname": params.get(u"last_name", u""),
            u"company": params.get(u"company", u""),
            u"email": params.get(u"email", u""),
            u"cc_emails": params.get(u"cc_emails", u""),
            u"phone": params.get(u"phone", u""),
            u"address_1": params.get(u"address_1", u""),
            u"address_2": params.get(u"address_2", u""),
            u"address_city": params.get(u"address_city", u""),
            u"address_state": params.get(u"address_state", u""),
            u"address_zip": params.get(u"address_zip", u""),
            u"address_country": params.get(u"address_country", u""),
            u"reference": params.get(u"reference", u"")
        }
        return self.request.post(endpoint=endpoint, payload=body)

    def delete(self, customer_id):
        u"""

        Delete a customer
        
        .. warning::

            Not implemented yet

        Given a customer_id::
        :return: = fattmerchant.Customer.delete("my_customer_id")

        """
        pass

    def find(self, customer_id, association_filter_id=None):
        u"""

        Find an customer, given a customer_id.

        :params customer_id: The customer id

        This does not return a result object. 

        .. note ::

            This will raise a :class:`NotFoundError <fattmerchant.exceptions.not_found_error.NotFoundError>` if the provided customer_id
            is not found.

        example

        .. code-block:: python

             customer = fattmerchant.Customer.find("my_customer_id")

        """
        endpoint = u"customer/{}".format(customer_id)
        return self.request.get(endpoint=endpoint)

    def payment_methods(self, customer_id):
        u"""

        Get payment methods for the customer
        """
        endpoint = u"customer/{}/payment-method".format(customer_id)
        payment_methods_customer = json.loads(
            self.request.get(endpoint=endpoint))
        logger.debug(payment_methods_customer)
        if payment_methods_customer is None:
            return list()
        else:
            return payment_methods_customer

    def update(self, customer_id, params={}):
        u"""

        Update an existing Customer
        By customer_id. The params are similar to create::
        :example: result = fattmerchant.Customer.update("my_customer_id", {
        "last_name": "Smith"
        })

        """
        endpoint = u'customer/{}'.format(id)
        body = {
            u"firstname": params.get(u"first_name", u""),
            u"lastname": params.get(u"last_name", u""),
            u"company": params.get(u"company", u""),
            u"email": params.get(u"email", u""),
            u"cc_emails": params.get(u"cc_emails", u""),
            u"phone": params.get(u"phone", u""),
            u"address_1": params.get(u"address_1", u""),
            u"address_2": params.get(u"address_2", u""),
            u"address_city": params.get(u"address_city", u""),
            u"address_state": params.get(u"address_state", u""),
            u"address_zip": params.get(u"address_zip", u""),
            u"address_country": params.get(u"address_country", u""),
            u"reference": params.get(u"reference")
        }
        return self.request.put(endpoint=endpoint, payload=body)
