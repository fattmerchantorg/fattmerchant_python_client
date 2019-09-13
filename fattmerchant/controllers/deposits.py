import json
import logging

from fattmerchant.exceptions import InvalidRequestDataException
from fattmerchant.models import DepositBatch, DepositBatchDetail

logger = logging.getLogger(__name__)


class DepositsController():
    """
    Class to allow interfacing with deposits within the Fattmerchant API
    """
    def __init__(self, request):
        self.request = request
        self.api = "fq"

    def list(self, options):
        """
        Gets a list of deposits within a certain date range from the API
        """

        if ("startDate" not in options and "endDate" not in options):
            msg = "At least a startDate or endDate" \
                " is required to make this request."

            raise InvalidRequestDataException(msg)

        endpoint = "deposit"
        response = json.loads(self.request.get(self.api, endpoint, options))

        deposits = []

        for deposit_data in response["data"]:
            deposits.append(DepositBatch(deposit_data))

        return deposits

    def get(self, options):
        """
        Gets a batch deposit's details within a certain date range from the API
        """

        if ("startDate" not in options):
            msg = "A startDate is required to perform this request."

            raise InvalidRequestDataException(msg)

        endpoint = "depositDetail"
        response = json.loads(self.request.get(self.api, endpoint, options))

        deposits = []

        for deposit_data in response["data"]:
            deposits.append(DepositBatchDetail(deposit_data))

        return deposits
