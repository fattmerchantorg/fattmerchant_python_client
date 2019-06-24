#!/bin/bash
"""
For definiting fattmerchant customer class
"""

__author__ = "tanmay.datta86@gmail.com"

from .inventory import CreditCard, Address, BankAccount
from FMRequestHelper import FMRequest

class CustomerApi():
    """
    Helper class for getting customer related information.
    """
    def __init__(self, api_key, merchant_id, request, company=None):
        self.api_key =  api_key
        self.request = request if request else FMRequest()
        #self.request.set_api_key(self.api_key)
        self.merchant_id = merchant_id
        self.company = company

    def __repr__(self):
        return """
            "for_company": {company} ,
            "merchant_id": {mid},
            """.format(
                company=self.company if self.company else "None",
                mid=self.merchant_id,
            )

    @staticmethod
    def all_customers():
        """ Return a collection of all customers. """
        pass

    def create(self, params):
        """
        Create a Customer
        No field is required::
        result = fattmerchant.Customer.create({
        "company": "Some company",
        "first_name": "John"
        })
        An example of creating an customer with all available fields::
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
        endpoint = 'customer'
        body = {
            "firstname": params.get("first_name", ""),
            "lastname": params.get("last_name", ""),
            "company": params.get("company", ""),
            "email": params.get("email", ""),
            "cc_emails": params.get("cc_emails", ""),
            "phone": params.get("phone", ""),
            "address_1": params.get("address_1", ""),
            "address_2": params.get("address_2", ""),
            "address_city": params.get("address_city", ""),
            "address_state": params.get("address_state", ""),
            "address_zip": params.get("address_zip", ""),
            "address_country": params.get("address_country", ""),
            "reference": params.get("reference","")
        }
        return self.request.post_request(endpoint=endpoint,
        body=body)


    def delete(self, customer_id):
        """
        Delete a customer
        Given a customer_id::
        result = fattmerchant.Customer.delete("my_customer_id")

        """
        pass

    def find(self, customer_id, association_filter_id=None):
        """
        Find an customer, given a customer_id.  This does not return a result
        object.  This will raise a :class:`NotFoundError <fattmerchant.exceptions.not_found_error.NotFoundError>` if the provided customer_id
        is not found. ::
        customer = fattmerchant.Customer.find("my_customer_id")
        """
        endpoint = "customer/{}".format(customer_id)
        return self.request.get_request(endpoint)
        
    def payment_methods_for(self, customer_id):
        """
        Find all payment methods for a given customer

        """
        endpoint = "customer/{}/payment-method".format(customer_id)
        return self.request.get_request(endpoint)

    def update(self, customer_id, params={}):
        """
        Update an existing Customer
        By customer_id. The params are similar to create::
        result = fattmerchant.Customer.update("my_customer_id", {
        "last_name": "Smith"
        })

        """
        endpoint = 'customer/{}'.format(id)
        body = {
            "firstname": params.get("first_name", ""),
            "lastname": params.get("last_name", ""),
            "company": params.get("company", ""),
            "email": params.get("email", ""),
            "cc_emails": params.get("cc_emails", ""),
            "phone": params.get("phone", ""),
            "address_1": params.get("address_1", ""),
            "address_2": params.get("address_2", ""),
            "address_city": params.get("address_city", ""),
            "address_state": params.get("address_state", ""),
            "address_zip": params.get("address_zip", ""),
            "address_country": params.get("address_country", ""),
            "reference": params.get("reference")
        }
        return self.request.put_request(endpoint=endpoint,
        body=body)
