import unittest
from unittest import mock
from os.path import dirname, join, abspath
from os import path
import json
from ddt import ddt, unpack, data
from fattmerchant.Merchant import Merchant
from fattmerchant.Customer import Customer
from fattmerchant.utils import compare_json_data
import logging


logger = logging.getLogger(__name__)
test_path = dirname(abspath(__file__))
static_data = join(test_path, "static_data")


def mocked_requests_put(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.text = json_data
            self.content = json_data
            self.status_code = status_code
    import pdb
    pdb.set_trace()

# This method will be used by the mock to replace requests.get


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.text = json_data
            self.content = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    import pdb
    pdb.set_trace()
    if args[0] == 'https://apidemo.fattlabs.com//self':
        with open(join(test_path, "mock_self.txt"), 'r') as mock_self:
            return MockResponse(mock_self.read(),
                                200)

    elif args[0] == 'https://apidemo.fattlabs.com//customer':
        with open(join(test_path, "mock_customer_list.txt"), 'r') as mock_customer_list:
            return MockResponse(mock_customer_list.read(), 200)

    return MockResponse(None, 404)


@ddt
class MerchantTests(unittest.TestCase):
    # @mock.patch('requests.get', side_effect=mocked_requests_get)
    # @mock.patch('requests.post', side_effect=mocked_requests_put)
    # @mock.patch('requests.put', side_effect=mocked_requests_put)
    # def setUp(self, mock_get, mock_post, mock_put):
    def setUp(self): #, mock_get, mock_post, mock_put):
        try:
            with open(os.path.join(dirpath,"static_data","API_KEY"), 'r') as key:
                self.api_key=key.read()
        except:
            print("Please create a file ==> 'API_KEY' with the correct API key before running the tests")

        merchant = Merchant(self.api_key)
        # merchant.request = mock.Mock()
        merchant.use_demo()
        merchant.update_merchant_info()
        self.merchant = merchant

    def test_creation_of_merchant(self):
        merchant = Merchant(self.api_key)
        merchant.use_demo()
        merchant.update_merchant_info()
        self.assertEqual(merchant.request.api_key, self.api_key)

    # @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_query_all_customers_of_merchant(self, mock_get):
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
    
    def test_merchant_team_list_api(self):
        answer = self.merchant.team_list_api_keys()
        with open(join(static_data, "get_api")) as file:
            expected_answer = json.load(file)
        print("expected is \n {}".format(expected_answer))
        self.assertDictEqual(answer, expected_answer)


    def test_tokenized_payment(self):
        logger.info("running")
        john_doe_token = "e1d3d2cc-5a3b-474f-a0f4-2dd16632b53f"
        john_doe_customer_id = "ef7304b3-7df7-4640-aabb-0191583290e2"
        payment_meta = dict()
        payment_meta["meta"] = {
            "tax": 2,
            "subtotal": 10,
            "lineItems": [
                {
                    "id": "optional-fm-catalog-item-id",
                    "item": "Demo Item",
                    "details": "this is a regular demo item",
                    "quantity": 10,
                    "price": .1
                }
            ]
        }
        payment_meta["total"] = 10
        payment_meta["pre_auth"] = ""
        answer = self.merchant.charge_customer_tokenized(john_doe_customer_id,
                                                         payment_meta)
        logger.info(
            "answer from charge customer via token ===> {}".format(answer))


if __name__ == '__main__':
    unittest.main()
