import unittest
from ddt import ddt, unpack, data
from fattmerchant.client import FMClient
import os

dirpath = os.path.dirname(__file__)

@ddt
class CustomerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(os.path.join(dirpath,"static_data","API_KEY"), 'r') as key:
            API_KEY=key.read()
        cls.fatt = FMClient(
            API_KEY,
            "prod")

    def test_creation_of_customerApi(self):
        customer = self.fatt.customers.list()
        print("customers retuned ==> {} \n".format(customer))
        self.assertIsInstance(customer, list)

    def test_transaction_list(self):
        transactions = self.fatt.transactions.list({ "page": 1 })
        print(transactions)
        try:
            transaction = self.fatt.transactions.get(transactions[0].id)
            print(repr(transaction))
            self.assertIsInstance(transaction, list)
        except:
            with self.assertRaises(IndexError):
                transactions[0]








if __name__ == '__main__':
    unittest.main()
