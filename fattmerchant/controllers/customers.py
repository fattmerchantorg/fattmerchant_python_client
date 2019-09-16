from __future__ import absolute_import
__author__ = "tanmay.datta86@gmail.com"

import logging
import json

from fattmerchant.exceptions import InvalidRequestDataException
from fattmerchant.models import Customer, PaymentMethod

logger = logging.getLogger(__name__)


class CustomersController(object):
    """
    Helper class for getting customer related information.
    """
    def __init__(self, request):
        self.request = request

    def create(self, payload):
        """
        Allows a merchant to create a customer through the API

        Parameters:
        payload (dict): A dict with all data necessary to create a customer
            example:
            {
                "firstname": "John",
                "lastname": "Smith",
                "company": "ABC INC",
                "email": "daniel@fattmerchant.com",
                "files": [],
                "phone": "1234567898",
                "address_1": "123 Rite Way",
                "address_2": "Unit 12",
                "address_city": "Orlando",
                "address_state": "FL",
                "address_zip": "32801",
                "address_country": "USA",
                "reference": "",
                "cc_emails": [],
                "notes": "",
                "allow_invoice_credit_card_payments": true
            }

        Returns: Customer object
        """

        endpoint = u'customer'
        required_fields = {"firstname", "lastname", "company", "email"}

        if not all(field in payload for field in required_fields):
            msg = "A dict with at least a firstname, lastname, email, " \
                "and company is required to perform this request."

            raise InvalidRequestDataException(msg)

        response = json.loads(
            self.request.post(endpoint=endpoint, payload=payload))

        return Customer(response)

    def list(self):
        """
        Gets a list of customers from the API
        """
        endpoint = "customer"

        response = json.loads(self.request.get(endpoint=endpoint))

        customers = []

        for customer_data in response["data"]:
            customers.append(Customer(customer_data))

        return customers

    def get(self, id=None):
        """
        Gets a single customer's details from the API
        """

        if not isinstance(id, (str, unicode)) or id is None:
            msg = "An id of type string has to be passed in with the request."

            raise InvalidRequestDataException(msg)

        endpoint = "customer/{}".format(id)
        response = self.request.get(endpoint=endpoint)

        return Customer(json.loads(response))

    def payment_methods(self, id=None):
        """
        Get all payment methods for a customer by customer ID from the API
        """

        if not isinstance(id, (str, unicode)) or id is None:
            msg = "An id of type string has to be passed in with the request."

            raise InvalidRequestDataException(msg)

        endpoint = "customer/{}/payment-method".format(id)

        response = json.loads(self.request.get(endpoint=endpoint))

        payment_methods = []

        for payment_method_data in response:
            payment_methods.append(PaymentMethod(payment_method_data))

        return payment_methods
