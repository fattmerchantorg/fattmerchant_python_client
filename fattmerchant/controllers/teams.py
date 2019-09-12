from __future__ import absolute_import

import json
import logging

__author__ = "austin.burns@fattmerchant.com"
logger = logging.getLogger(__name__)


class TeamsController():
    """
    Class to interface with the team resource in the Core API
    """
    def __init__(self, request):
        self.request = request

    def _create_team(self, payload):
        """
        This call makes creates a new team

        Parameters:
        payload (dict): A dictionary with all data necessary to create a team
            example:
            {
                "company_name": "Fattmerchant",
                "contact_name": "Fattmerchant",
                "contact_email": "info2@fattmerchant.com",
                "contact_phone": "8555503288",
                "address_1": "25 Wall Street",
                "address_2": "Suite 1",
                "address_city": "Orlando",
                "address_state": "FL",
                "address_zip": "32801"
            }

        Returns:
        tuple: ({team temporary api key}, {user team belongs to}, {team data})
        """

        endpoint = "team"
        response = json.loads(
            self.request.post(endpoint=endpoint, payload=payload))

        try:
            latestTeam = response[0]

            for team in response:
                if team['merchant']['created_at'] > latestTeam['merchant'][
                        'created_at']:
                    latestTeam = team

            return (latestTeam['token'], latestTeam['user'],
                    latestTeam['merchant'])
        except IndexError:
            logger.error("The team was not able to be created")

            return []

    def create(self, payload):
        """
        This call makes creates a new team

        Parameters:
        payload (dict): A dictionary with all data necessary to create a team
            example:
            {
                "company_name": "Fattmerchant",
                "contact_name": "Fattmerchant",
                "contact_email": "info2@fattmerchant.com",
                "contact_phone": "8555503288",
                "address_1": "25 Wall Street",
                "address_2": "Suite 1",
                "address_city": "Orlando",
                "address_state": "FL",
                "address_zip": "32801"
            }

        Returns:
        tuple: ({team permanent api key}, {team data})
        """

        token, user, team = self._create_team(payload)

        endpoint = "team/apikey"
        payload = {
            "team_role": user['team_role'],
            "name": "{} API Key".format(team['company_name'])
        }

        response = json.loads(
            self.request.post(endpoint=endpoint, payload=payload))

        return (response['api_key'], team)
