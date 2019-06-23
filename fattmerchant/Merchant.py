"""
#!/bin/bash

For definiting fattmerchant merhcant class
"""

__author__ = "tanmay.datta86@gmail.com"

from .Customer import CustomerApi
from FMRequestHelper import FMRequest


class Merchant:
    def __init__(self, api_key, id, company = None):
        self.api_key = api_key
        self.id = id
        self.request = FMRequest()
        #self.request.set_api_key(self.api_key)
        self.company = company
        self.customers = CustomerApi(api_key, self.id, self.request,
        self.company)
    
    def items(self):
        endpoint = "items"
        self.request.get_request(endpoint)
    
    def get_items_by_code(self):
        endpoint = "item/code"
        self.request.get_request(endpoint)

