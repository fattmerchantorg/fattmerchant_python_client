import unittest
from os.path import dirname, join
from ddt import ddt, unpack, data
from fattmerchant.Merchant import Merchant

@ddt
class MerchantTests(unittest.TestCase):
    def setUp(self):
        filepath = join(dirname(__file__), "..", "fattmerchant", "test_api_key.txt")
        with open(filepath) as api_file:
            self.api_key  = api_file.read()

        merchant = Merchant("None", 123, None)
        merchant.api_key = self.api_key
        self.merchant = merchant
        

    def test_creation_of_merchant(self):
        merchant = Merchant("None", 123, None)
        self.assertEqual(merchant.request.api_key, self.api_key)
    
    def test_getting_request(self):
        print(self.merchant.items())
        


if __name__ == '__main__':
    unittest.main()