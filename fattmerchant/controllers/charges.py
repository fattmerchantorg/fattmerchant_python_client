import json
import logging

from fattmerchant.exceptions import InvalidRequestDataException
from fattmerchant.models import Transaction

logger = logging.getLogger(__name__)


class ChargesController(object):
    """
    Class to allow interfacing with charges within the Fattmerchant API
    """
    def __init__(self, request):
        self.request = request

    def create(self, id=None, meta=None, total=None, pre_auth=None):
        """
        Creates a charge for a merchant through the API

        :param id: A payment method ID
        :type id: string
        :param meta: Any meta data for the payment *i.e. tax*
        :type meta: dict
        :param total: The total amount to charge
        :type total: float
        :param pre_auth: Whether or not to confirm funds exist
        :type pre_auth: boolean

        :return: A single transaction object
        :rtype: :doc:`../models/transaction`

        :raise InvalidRequestDataException: Raised if **id** is not
            provided or **meta** is not provided or **total** is not provided

        """

        if id is None or not isinstance(id, (str, unicode)):
            msg = "An id of type string is required to complete the request."

            raise InvalidRequestDataException(msg)

        if meta is None or not isinstance(meta, dict):
            msg = "A meta object of type dict is required to complete " \
                "the request."

            raise InvalidRequestDataException(msg)

        if total is None or not isinstance(total, (int, float)):
            msg = "A total of type int or float is required to complete " \
                "the request."

            raise InvalidRequestDataException(msg)

        endpoint = "charge"

        payload = {"payment_method_id": id, "meta": meta, "total": total}

        if pre_auth is not None:
            payload["pre_auth"] = pre_auth

        response = json.loads(
            self.request.post(endpoint=endpoint, payload=payload)
        )

        return Transaction(response)
