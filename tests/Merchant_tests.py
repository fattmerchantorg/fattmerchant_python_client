import unittest
from os.path import dirname, join
from ddt import ddt, unpack, data
from fattmerchant.Merchant import Merchant
from fattmerchant.Customer import Customer
import logging

logger = logging.getLogger(__name__)

@ddt
class MerchantTests(unittest.TestCase):
    def setUp(self):
        filepath = join(dirname(__file__), "..", "fattmerchant", "test_api_key.txt")
        with open(filepath) as api_file:
            self.api_key  = api_file.read()

        merchant = Merchant(self.api_key)
        merchant.use_demo()
        merchant.update_merchant_info()
        self.merchant = merchant
        

    def test_creation_of_merchant(self):
        merchant = Merchant(self.api_key)
        merchant.use_demo()
        merchant.update_merchant_info()
        self.assertEqual(merchant.request.api_key, self.api_key)

    def test_query_all_customers_of_merchant(self):
        all_customers = self.merchant.get_all_customers()
        logger.info(all_customers)
    
    def test_adding_new_customer(self):
        customer_data = {
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
        customer = Customer(customer_info=customer_data)
        answer = self.merchant.add_customer(customer)
        self.assertEqual(answer["id"], "59327746-fbca-4fb6-adf0-e88c99245548")

    def test_getting_request(self):
        print(self.merchant.items())
    def test_tokenized_payment(self):
        logger.info("rnning")
        john_doe_token = "e1d3d2cc-5a3b-474f-a0f4-2dd16632b53f"
        john_doe_customer_id = "ef7304b3-7df7-4640-aabb-0191583290e2"
        payment_meta = dict()
        payment_meta["meta"] = {
            "tax":2,
            "subtotal":10,
            "lineItems": [
                {
                    "id": "optional-fm-catalog-item-id",
                    "item":"Demo Item",
                    "details":"this is a regular demo item",
                    "quantity":10,
                    "price": .1
                }
            ]
        }
        payment_meta["total"] = 10 
        payment_meta["pre_auth"] = ""
        answer = self.merchant.charge_customer_tokenized(john_doe_customer_id, payment_meta)
        logger.info("answer from charge customer via tokene ===> {}".format(answer))
        


if __name__ == '__main__':
    unittest.main()
