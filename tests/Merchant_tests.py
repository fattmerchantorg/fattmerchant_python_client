import unittest
from ddt import ddt, unpack, data
from fattmerchant.Merchant import Merchant

@ddt
class MerchantTests(unittest.TestCase):
    def test_creation_of_merchant(self):
        merchant = Merchant("None", 123, None)
        print(merchant)
        


if __name__ == '__main__':
    unittest.main()