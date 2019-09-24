import json
import logging

from fattmerchant.exceptions import InvalidRequestDataException, \
    ResourceNotCreatedException
from fattmerchant.models import Team

logger = logging.getLogger(__name__)


class TeamsController(object):
    """
    Class to interface with the team resource in the Core API
    """
    def __init__(self, request):
        self.request = request

    def _create_team(self, payload):
        """
        Private method to make the API call to create a new team

        Args:
            payload (dict): A dictionary with all data necessary to create a
                team

        Returns:
            tuple: A tuple with an api key, a user for a merchant, and said
                merchant

        Raises:
            ResourceNotCreatedException: If the team couldn't be accessed
                then it wasn't able to be created

        """

        endpoint = "team"
        response = json.loads(
            self.request.post(endpoint=endpoint, payload=payload)
        )

        try:
            latestTeam = response[0]

            for team in response:
                if (
                    team["merchant"]["created_at"] >
                    latestTeam["merchant"]["created_at"]
                ):
                    latestTeam = team

            return (
                latestTeam["token"], latestTeam["user"], latestTeam["merchant"]
            )
        except IndexError:
            logger.error("The team was not able to be created")

            raise ResourceNotCreatedException

    def create(self, payload):
        """
        Creates a new team through the API

        :param payload: A dictionary with all data necessary to create a team

            .. note:: **company_name** and **company_email** are required
            .. code-block:: JSON

                {
                    "company_name": "Fattmerchant",
                    "comtact_name": "Fattmerchant",
                    "contact_email": "info2@fattmerchant.com",
                    "contact_phone": "8555503288",
                    "display_name": "Fattmerchant",
                    "address_1": "25 Wall Street",
                    "address_2": "Suite 1",
                    "address_city": "Orlando",
                    "address_state": "FL",
                    "address_zip": "32801",
                    "options": {}
                }

        :type payload: dict

        :return: A tuple with a team object and said team's api key
        :rtype: (:doc:`../models/team`, string)

        :raise InvalidRequestDataException: Raised if **company_name** is not
            provided or **contact_email** is not provided

        :raise ResourceNotCreatedException: Raised if the team could not be
            created within the API

        """

        if "company_name" not in payload or not isinstance(
            payload["company_name"], (str, unicode)
        ):
            msg = "A company name of type string is required to complete the \
                request."

            raise InvalidRequestDataException(msg)

        if "contact_email" not in payload or not isinstance(
            payload["contact_email"], (str, unicode)
        ):
            msg = "A contact email of type string is required to complete the \
                request."

            raise InvalidRequestDataException(msg)

        token, user_data, team_data = self._create_team(payload)

        endpoint = "team/apikey"
        payload = {
            "team_role": user_data["team_role"],
            "name": "{} API Key".format(team_data["company_name"]),
        }

        response = json.loads(
            self.request.post(endpoint=endpoint, payload=payload)
        )

        return (response["api_key"], Team(team_data))
