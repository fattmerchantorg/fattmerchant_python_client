#!/bin/bash
"""
For definiting fattmerchant customer class
"""

__author__ = "tanmay.datta86@gmail.com"

from .inventory import CreditCard, Address, BankAccount
from .FMRequestHelper import FMRequest
import logging

logger = logging.getLogger(__name__)

class CustomerApi():
    """
    Helper class for getting customer related information.
    """

    def __init__(self, api_key, merchant_id=None,
                 request=None, company=None):
        logging.debug("creating customer")
        self.api_key = api_key
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

class Customer:
    """
    The customer object given by the fatterchant api
    """
    def __init__(self,customer_info, merchant_id=None):

        """
        try to initiate a customer object with sane defaults
        """
        self.merchant_id = merchant_id # nothing should work without it in theory
        self.id = customer_info.get("id", None)
        self.firstname = customer_info.get("firstname", None)
        self.lastname = customer_info.get("lastname", None)
        self.company = customer_info.get("company", None)
        self.email = customer_info.get("email", None)
        self.cc_emails = customer_info.get("cc_emails", None)
        self.phone = customer_info.get("phone", None)
        self.address_1 = customer_info.get("address_1", None)
        self.address_2 = customer_info.get("address_2", None)
        self.address_city = customer_info.get("address_city", None)
        self.address_state = customer_info.get("address_state", None)
        self.address_zip = customer_info.get("address_zip", None)
        self.address_country = customer_info.get("address_country", None)
        self.notes = customer_info.get("notes", None)
        self.reference = customer_info.get("reference", None)
        self.options = customer_info.get("options", None)
        self.created_at = customer_info.get("created_at", None)
        self.updated_at = customer_info.get("updated_at", None)
        self.deleted_at = customer_info.get("deleted_at", None)
        self.gravatar = customer_info.get("gravatar", None)

    def __repr__(self):
        return """
            "merchant": {mer} ,
            "first name": {fname},
            "last name": {lname},
            "email": {email},
            """.format(
                mer=self.merchant_id,
                fname=self.firstname,
                lname=self.lastname,
                email=self.email,
            )
