import json
import logging

from fattmerchant.exceptions import InvalidRequestDataException
from fattmerchant.models import DepositBatch, DepositDetails

logger = logging.getLogger(__name__)


class DepositsController(object):
    """
    Class to interface with deposits within the Fattmerchant API
    """
    def __init__(self, request):
        self.request = request
        self.api = "fq"

    def list(self, options):
        """
        Gets a list of deposit batches within a certain date range from the API

        :param options: A dictionary with any optional query params

            .. note:: **start_date** or **end_date** is required
            .. code-block:: json

                {
                    "start_date": "1970-01-01",
                    "end_date": "1970-01-01",
                    "timezone": "EST",
                    "timezoneOffset": 0
                }

        :type options: dict

        :return: A list of deposit batch objects
        :rtype: :doc:`../models/deposit_batch`

        :raise InvalidRequestDataException: Raised if **start_date** is not
            provided or **end_date** is not provided

        """

        # yapf: disable
        if (
            "start_date" not in options
                or not isinstance(options["start_date"], (str, unicode))
            and "end_date" not in options
                or not isinstance(options["end_date"], (str, unicode))
        ):
            # yapf: enable
            msg = "At least a start_date or end_date is required to " \
                "make this request."

            raise InvalidRequestDataException(msg)

        # Change the date keys to keys the API accepts
        options["startDate"] = options.pop("start_date")
        options["endDate"] = options.pop("end_date")

        endpoint = "deposit"
        response = json.loads(self.request.get(self.api, endpoint, options))

        deposits = []

        for deposit_data in response["data"]:
            deposits.append(DepositBatch(deposit_data))

        return deposits

    def get(self, options):
        """
        Gets a list of deposit batch details within a certain date range from \
        the API

        :param options: A dictionary with any optional query params

            .. note:: **start_date** or **end_date** is required
            .. code-block:: json

                {
                    "start_date": "1970-01-01",
                    "end_date": "1970-01-01",
                    "timezone": "EST",
                    "timezoneOffset": 0
                }

        :type options: dict

        :return: A list of deposit details objects
        :rtype: :doc:`../models/deposit_details`

        :raise InvalidRequestDataException: Raised if **start_date** is not
            provided or **end_date** is not provided

        """

        # yapf: disable
        if (
            "start_date" not in options
                or not isinstance(options["start_date"], (str, unicode))
            and "end_date" not in options
                or not isinstance(options["end_date"], (str, unicode))
        ):
            # yapf: enable
            msg = "At least a start_date or end_date is required to " \
                "make this request."

            raise InvalidRequestDataException(msg)

        # Change the date keys to keys the API accepts
        options["startDate"] = options.pop("start_date")
        options["endDate"] = options.pop("end_date")

        endpoint = "depositDetail"
        response = json.loads(self.request.get(self.api, endpoint, options))

        deposits = []

        for deposit_data in response["data"]:
            deposits.append(DepositDetails(deposit_data))

        return deposits
