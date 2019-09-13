import json
import logging

from fattmerchant.models import Transaction

logger = logging.getLogger(__name__)


class ChargesController():
    """
    Class to allow interfacing with charges within the Fattmerchant API
    """
    def __init__(self, request):
        self.request = request

    def create(self, payment_method_id, data):
        """
        Allows a merchant to charge a customer through the API
        with a payment method id
        """
        endpoint = "charge"

        payload = {
            "payment_method_id": payment_method_id,
            "meta": data["meta"],
            "total": data["total"],
            "pre_auth": data["pre_auth"]
        }

        response = json.loads(
            self.request.post(endpoint=endpoint, payload=payload))

        return Transaction(response)
