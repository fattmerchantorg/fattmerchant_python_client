import json
import logging

from fattmerchant.exceptions import InvalidRequestDataException
from fattmerchant.models import Transaction

logger = logging.getLogger(__name__)


class TransactionsController():
    """
    Class to allow interfacing with transactions within the Fattmerchant API
    """
    def __init__(self, request):
        self.request = request

    def list(self, options={}):
        """
        Gets a list of transactions from the API
        """

        endpoint = "transaction"
        response = json.loads(
            self.request.get(endpoint=endpoint, options=options)
        )

        transactions = []

        for transaction_data in response["data"]:
            transactions.append(Transaction(transaction_data))

        return transactions

    def get(self, id=None):
        """
        Gets a single transaction's details from the API
        """

        if not isinstance(id, (str, unicode)) or id is None:
            msg = "An id of type string has to be passed in with the request."

            raise InvalidRequestDataException(msg)

        endpoint = "transaction/{}".format(id)
        response = self.request.get(endpoint=endpoint)

        return Transaction(json.loads(response))

    def refund(self, id=None, amount=None):
        """
        Refund a certain amount of a transaction
        """

        if not isinstance(id, (str, unicode)) or id is None:
            msg = "An id of type string has to be passed in with the request."

            raise InvalidRequestDataException(msg)

        if not isinstance(amount, (int, float)) or amount is None:
            msg = "An amount of type int or float has to be passed " \
                "in with the request."

            raise InvalidRequestDataException(msg)

        endpoint = "transaction/{}/refund".format(id)
        payload = {"total": amount}

        response = self.request.post(endpoint=endpoint,
                                     payload=payload)

        return Transaction(json.loads(response))
