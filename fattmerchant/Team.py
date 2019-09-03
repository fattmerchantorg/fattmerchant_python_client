# -*- coding: utf-8 -*-
from __future__ import absolute_import

import json
import logging

__author__ = "austin.burns@fattmerchant.com"
logger = logging.getLogger(__name__)


class Team():
    """
    Class to interface with the team resource in the Core API
    """
    def __init__(self, api_key, request):
        self.api_key = api_key
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

    # TODO: Finish the team endpoints

    # def edit_info(self, team_info):
    #     """
    #     This function allows a user to edit the information,
    #     such as address and name, of a merchant team.
    #     This only works for team members with admin as their team_role.
    #     This call does not change team member information.

    #     Arguments:
    #         team_info {dict} -- team_info json/dict object

    #     example

    #     .. code-block:: JSON

    #         {
    #         "company_name": "Fattmerchant",
    #         "contact_name": "Fattmerchant",
    #         "contact_email": "info2@fattmerchant.com",
    #         "contact_phone": "8555503288",
    #         "address_1": "25 Wall Street",
    #         "address_2": "Suite 1",
    #         "address_city": "Orlando",
    #         "address_state": "FL",
    #         "address_zip": "32801"
    #         }

    #     .. note::
    #         Authentication Token and Team Admin Status Required

    #     """
    #     endpoint = "team"
    #     answer = self.request.put(endpoint=endpoint, payload=team_info)
    #     logger.debug(json.loads(answer))
    #     return json.loads(answer)

    # def edit_branding_info(self, branding_info):
    #     """somethign

    #     .. note::
    #         Authentication Token and Team Admin Status Required

    #     This resource gives merchant admins the ability to change their company's branding.
    #     branding may be uploaded as either a PNG or JPEG image file.
    #     A merchant's branding will appear anywhere a merchant's object is returned.
    #     The merchant branding will be securely hosted on Amazon S3 bucket and recorded in our database.

    #     Arguments:
    #         branding_info {dict} -- [description]

    #     example

    #     .. code-block:: JSON

    #         {
    #             "name": "Mercedes-Benz",
    #             "image": "logo.png"
    #         }

    #     """
    #     endpoint = "team/option/branding"
    #     answer = self.request.put(endpoint=endpoint, payload=branding_info)
    #     logger.debug(json.loads(answer))
    #     return json.loads(answer)

    # def list_members(self):
    #     """
    #     .. note::
    #         Authentication Token and Team Admin Status Required

    #     Retrieves all the users on a merchants's team, showing team-oriented details and team_role.
    #     Used for finding all members of a team and listing them by roles.
    #     """
    #     endpoint = "team/user"
    #     answer = self.request.get(endpoint=endpoint)
    #     logger.debug(json.loads(answer))
    #     return json.loads(answer)

    # def create_member(self, user_info):
    #     """
    #     .. note::
    #         Authentication Token and Team Admin Status Required

    #     This creates a whole new user account in your merchant team.
    #     Automatically adds the user to the merchant team.
    #     Can only be used by users with team_rule of "admin".
    #     This is one of two ways to create a new user account; the other being POST /self.
    #     Requires a valid email, password and name at minimum.
    #     If team_role is not selected, it will default to "full".
    #     Used by team admins who want to add members to their merchant account who do not already have a Fattmerchant account.

    #     Arguments:
    #         user_info {[type]} -- user information in a dictionary

    #     example

    #     .. code-block:: JSON

    #         {
    #         "email": "daniel+1024@fattmerchant.com",
    #         "password": "bottomline",
    #         "password_confirmation": "bottomline",
    #         "name": "Bob Dylan",
    #         "team_role": "full",
    #         "team_enabled": true,
    #         "send_verification_email": true,
    #         "url": "https://omni.fattmerchant.com/#/verify/"
    #         }
    #     """
    #     endpoint = "team/user"
    #     answer = self.request.put(endpoint=endpoint, payload=user_info)
    #     logger.debug(json.loads(answer))
    #     return json.loads(answer)

    # def create_api_key_user(self, name, role):
    #     """creates api key

    #     .. note::
    #         Authentication Token and Team Admin Status Required

    #     This creates a whole new user account in your merchant team which will have is_api_key = true.
    #     This will also return the api key value.

    #     Arguments:
    #         name {str} -- name for api key
    #         role {str} -- role of the api key user

    #     example

    #     .. code-block:: python

    #         team_create_api_key("do not delete - zapier key", "admin")

    #     """
    #     endpoint = "team/apikey"
    #     api_key_info = {"team_role": role, "name": name}
    #     answer = self.request.put(endpoint=endpoint, payload=api_key_info)
    #     logger.debug(json.loads(answer))
    #     return json.loads(answer)

    # def list_api_keys(self):
    #     """lists all api keys

    #     .. note::
    #         Authentication Token and Team Admin Status Required

    #     List out all team member user records which are api keys.

    #     """
    #     endpoint = "team/apikey"
    #     answer = self.request.get(endpoint=endpoint)
    #     try:
    #         json_answer = json.loads(answer)
    #         logger.debug(json_answer)
    #         return json_answer
    #     except Exception, e:
    #         logger.critical("error ==> {}".format(e))
    #         return None

    # def get_user_by_id(self, id):
    #     """user info by id

    #     .. note::
    #         Authentication Token and Team Admin Status Required

    #     Retrieves the team member that matches the given id.
    #     Deploys information on the team member, including their team_role.
    #     Used in conjunction with PUT /team/user/{id} to edit a team member.
    #     Requires team_role of admin to use.

    #     Arguments:
    #         id {str} -- user_id

    #     """
    #     endpoint = "team/user/{}".format(id)
    #     answer = self.request.get(endpoint=endpoint)
    #     logger.debug(json.loads(answer))
    #     return json.loads(answer)

    # def update_user_by_id(self, id, user_info):
    #     """updates user info

    #     .. note::
    #         Authentication Token and Team Admin Status Required

    #     Allows team admins to change a team members information, such as role.
    #     Used in conjunction with GET /team/user/{id} to view a team members information.
    #     This can be used to remove a member from the team.
    #     Can only be used by members with team_role of "admin.

    #     Arguments:
    #         id {str} -- user_id
    #         user_info {dict} -- user_info

    #     example:

    #     .. code-block:: JSON

    #         {
    #             "id": "21a64e9e-3c13-4b85-9f85-67cb4fda808a",
    #             "system_admin": false,
    #             "name": "WILLIAM II KOHLS",
    #             "email": "daniel+1002@fattmerchant.com",
    #             "email_verification_sent_at": null,
    #             "email_verified_at": null,
    #             "created_at": "2017-05-15 19:31:35",
    #             "updated_at": "2017-05-15 19:41:53",
    #             "deleted_at": null,
    #             "gravatar": "//www.gravatar.com/avatar/4d6b3ceb5b37b610a68ef23fcbe0060b",
    #             "team_role": "admin",
    #             "team_admin": true,
    #             "team_enabled": true
    #             }

    #     """

    #     endpoint = "team/user/{}".format(id)
    #     answer = self.request.put(endpoint=endpoint, payload=user_info)
    #     logger.debug(json.loads(answer))
    #     return json.loads(answer)

    # def update_settings(self, settings):
    #     """updates team settings

    #     .. note::
    #         Authentication Token and Team Admin Status Required

    #     Adds team options, also known as team settings, to a team.
    #     Saved as "options" under a team in the database.
    #     This doesn't affect the values of the options at all.
    #     Returns the results of the modified team options.
    #     Only members with team_role of "admin" can use this.
    #     Also used by hosted payments to change hosted payment options.

    #     Arguments:
    #         settings {dict} -- setting dictionary/json more info below

    #     Available Team Options

    #     - hosted_payments_token - Changes the hosted_payments token/URL.
    #     - hosted_payment_note - This changes the hosted_payments_note's page memo.
    #     - hosted_payments_success_note - Changes the hosted_payments_note's success message.
    #     - gateway - This changes the merchant's gateway.
    #         Currently available gateways are test and authorize_net.
    #         Gateways change where the user information will go through.
    #     - plan - Changes the merchant's plan.
    #             Plans are preset information chosen by a merchant to set a
    #             course for their merchant account.
    #             Either basic, plus and premium are available.
    #             Each option will affect the merchant's functionality within
    #             the Fattmerchant system.
    #             Each plan may cost the merchant differently.
    #     - receipts_email - Add/updates emails to be given a receipt when a hosted_payment goes through.

    #     team Options For Mobile and Batch Over EMV Gateway
    #     Used by the mobile app to store sensitive account information regarding the card reader and the EMV gateway.

    #     - mv_terminal_id - The ID for the EMV gateway.
    #     - mv_terminal_secret - Specific settings necessary for the card reader.
    #     - mv_user - transmits the user's username over the EMV gateway.
    #     - mv_password - transmits the user's password over the EMV gateway.

    #     example:

    #     .. code-block:: JSON

    #         [
    #             {
    #                 "name": "hosted_payments_token",
    #                 "url": "http://localhost.app:5477/#/pay/",
    #                 "value": "BARTLE-_"
    #             },
    #             {
    #                 "name": "hosted_payments_success_note",
    #                 "value": "Success Note"
    #             },
    #             {
    #                 "name": "hosted_payments_note",
    #                 "value": "Page Memo"
    #             }
    #         ]

    #     """
    #     endpoint = "team/option"
    #     answer = self.request.put(endpoint=endpoint, payload=settings)
    #     logger.debug(json.loads(answer))
    #     return json.loads(answer)

    # def update_registration_data(self, registration_data):
    #     pass

    # def change_plan(self, plan):
    #     """changes team plan

    #     .. note::
    #         Authentication Token and Team Admin Status Required

    #     This function changes the merchant team's plan.
    #     Merchant teams have a plan they can set that affects the functionality of their account.
    #     There are two plan types: PORTAL and PREMIUM.
    #     Different plans have different payment options and processing.
    #     Plans on affects what API calls can be made.
    #     This can only be called by a team admin.

    #     Available Team Plans
    #     - PORTAL - has access to reporting, transactions and team in the API.
    #     - PREMIUM - has access to everything in the API.

    #     Arguments:
    #         plan {str} -- plan description --> {"portal"/"premium"}
    #     """
    #     endpoint = "team/option/plan"
    #     body = {"plan": plan.upper()}
    #     answer = self.request.put(endpoint=endpoint, payload=body)
    #     logger.debug(json.loads(answer))
    #     return json.loads(answer)

    # def change_gateway(self, gateway):
    #     """Changes teams gateway

    #     .. note::
    #         Authentication Token and Team Admin Status Required

    #     Gateways are the pathways chosen by users to decide where they need their information to go through.
    #     Currently available gateways are test and authorize_net.
    #     This process changes the user's gateway to another one using a login and password.
    #     Can only be changed by team members with team_role of "admin".
    #     Newly created teams that haven't registered a gateway with this function will automatically have gateway_name and gateway_type set to null.

    #     Arguments:
    #         gateway {str} -- gateway string
    #     """
    #     endpoint = "team/option/gateway"
    #     body = {"value": gateway.upper()}
    #     answer = self.request.put(endpoint=endpoint, payload=body)
    #     logger.debug(json.loads(answer))
    #     return json.loads(answer)

    # """
    # Class to allow interfacing with deposits within the Fattmerchant API
    # """
    # def __init__(self, api_key, request):
    #     self.api_key = api_key
    #     self.request = request
    #     self.api = "fq"

    # def list(self, options):
    #     """
    #     Gets a list of deposits within a certain fate range from the API
    #     """

    #     if ("startDate" not in options and "endDate" not in options):
    #         msg = "At least startDate or endDate \
    #                are required to make this request"

    #         raise AttributeError(msg)

    #     endpoint = "deposit"
    #     response = json.loads(self.request.get(self.api, endpoint, options))

    #     try:
    #         logger.debug(response)

    #         return json.dumps(response['data'])
    #     except AttributeError:
    #         logger.error(
    #             "Unable to make request with options: {}".format(options))

    # def get(self, options):
    #     """
    #     Gets a batch deposit's details within a certain date range from the API
    #     """

    #     if ("startDate" not in options):
    #         msg = "A startDate is required to perform this request"

    #         raise AttributeError(msg)

    #     endpoint = "depositDetail"
    #     response = json.loads(self.request.get(self.api, endpoint, options))

    #     try:
    #         logger.debug(response)

    #         return json.dumps(response['data'])
    #     except AttributeError:
    #         logger.error("The deposit id that was passed in is invalid")
