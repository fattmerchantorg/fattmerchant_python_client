"""
#!/bin/bash

For definiting fattmerchant customer class
"""

__author__ = "tanmay.datta86@gmail.com"

from .inventory import CreditCard, Address, BankAccount
from FMRequestHelper import FMRequest

class Customer():
    """
    A class representing a customer.
    An example of creating an customer with all available fields::
    {
        "firstname": "John",
        "lastname": "Smith",
        "company": "ABC INC",
        "email": "demo@fattmerchant.com",
        "cc_emails": [
            "daniel@fattmerchant.com"
        ],
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
    def __init__(self, attributes):
        self.payment_methods = []
        self.api_key =  attributes['api_key']
        self.request = FMRequest()
        #self.request.set_api_key(self.api_key)
        self.merchant_id = attributes['merchant_id']
        if "credit_cards" in attributes:
            self.credit_cards = [CreditCard(**credit_card) for credit_card in self.credit_cards]
            self.payment_methods += self.credit_cards
        if "addresses" in attributes:
            self.addresses = [Address(**address)
                              for address in self.addresses]

        if "bank_accounts" in attributes:
            self.bank_accounts = [BankAccount(**bank_account) for bank_account in self.bank_accounts]
            self.payment_methods += self.bank_accounts

    def __repr__(self):
        return """
            "id": {id}
            "company": {company} ,
            "created_at": {created_at},
            "email": {email},
            "first_name": {fname},
            "last_name": {lname},
            "merchant_id": {mid},
            "phone": {phone},
            "updated_at": {updated_at},
            """.format(
                id=self.id,
                company=self.company,
                email=self.email,
                fname=self.first_name,
                lname=self.last_name,
                mid=self.merchant_id,
                phone=self.phone,
                updated_at=self.updated_at
            )

    @staticmethod
    def all_customers():
        """ Return a collection of all customers. """
        pass

    @staticmethod
    def create(params={}):
        """
        Create a Customer
        No field is required::
            result = fattmerchant.Customer.create({
                "company": "Some company",
                "first_name": "John"
            })
        """
        endpoint = 'customer'
        body = {
            "firstname": self.first_name,
            "lastname": self.last_name,
            "company": self.company,
            "email": self.email,
            "cc_emails": self.cc_emails,
            "phone": self.phone
            "address_1": self.address_1,
            "address_2": self.address_2,
            "address_city": self.address_city,
            "address_state": self.address_state,
            "address_zip": self.address_zip,
            "address_country": self.address_country,
            "reference": self.reference
        }
        return self.request.post_request(endpoint=endpoint,
        body=body)


    @staticmethod
    def delete(customer_id):
        """
        Delete a customer
        Given a customer_id::
            result = fattmerchant.Customer.delete("my_customer_id")
        """
        pass

    def find(customer_id, association_filter_id=None):
        """
        Find an customer, given a customer_id.  This does not return a result
        object.  This will raise a :class:`NotFoundError <fattmerchant.exceptions.not_found_error.NotFoundError>` if the provided customer_id
        is not found. ::
            customer = fattmerchant.Customer.find("my_customer_id")
        """
        endpoint = "customer/{}".format(self.id)
        return self.request.get_request(endpoint)
        


    @staticmethod
    def update(customer_id, params={}):
        """
        Update an existing Customer
        By customer_id. The params are similar to create::
            result = fattmerchant.Customer.update("my_customer_id", {
                "last_name": "Smith"
            })
        """
        endpoint = 'customer/{}'.format(id)
        body = {
            "firstname": self.first_name,
            "lastname": self.last_name,
            "company": self.company,
            "email": self.email,
            "cc_emails": self.cc_emails,
            "phone": self.phone
            "address_1": self.address_1,
            "address_2": self.address_2,
            "address_city": self.address_city,
            "address_state": self.address_state,
            "address_zip": self.address_zip,
            "address_country": self.address_country,
            "reference": self.reference
        }
        return self.request.put_request(endpoint=endpoint,
        body=body)

    # @staticmethod
    # def create_signature():
    #     return [
    #         "company", "email", "fax", "first_name", "id", "last_name", "phone", "website", "device_data", "device_session_id", "fraud_merchant_id", "payment_method_nonce",
    #         {"risk_data": ["customer_browser", "customer_ip"]},
    #         {"custom_fields": ["__any_key__"]},
    #         {"options": [{"paypal": [
    #             "payee_email",
    #             "order_id",
    #             "custom_field",
    #             "description",
    #             "amount",
    #         ]}]},
    #     ]

    # @staticmethod
    # def update_signature():
    #     return [
    #         "company", "email", "fax", "first_name", "id", "last_name", "phone", "website", "device_data", "device_session_id", "fraud_merchant_id", "payment_method_nonce", "default_payment_method_token",
    #         {"custom_fields": ["__any_key__"]},
    #         {"options": [{"paypal": [
    #             "payee_email",
    #             "order_id",
    #             "custom_field",
    #             "description",
    #             "amount",
    #         ]}]},
    #     ]
