from __future__ import absolute_import
__author__ = "daniel@fattmerchant.com"

import logging
import json

from fattmerchant.exceptions import InvalidRequestDataException
from fattmerchant.models import PaymentMethod

logger = logging.getLogger(__name__)


class PaymentMethodsController(object):
    """
    Class to interface with the payment method resource in the Core API
    """
    def __init__(self, request):
        self.request = request

    def get(self, id=None):
        """
        Gets a single payment methods's details from the API by id

        :param id: A payment-method ID
        :type id: string

        :return: A single payment-method object
        :rtype: :doc:`../models/paymentmethod`

        :raise InvalidRequestDataException: Raised if **id** is not provided

        """

        if not isinstance(id, (str, unicode)) or id is None:
            msg = "An id of type string has to be passed in with the request."

            raise InvalidRequestDataException(msg)

        endpoint = "payment-method/{}".format(id)
        response = self.request.get(endpoint=endpoint)

        return PaymentMethod(json.loads(response))
