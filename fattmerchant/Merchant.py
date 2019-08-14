# -*- coding: utf-8 -*-
"""
For defining helper classes for fattmerchant merchant behaviour
"""

from __future__ import absolute_import

import json
import logging

from .Customer import Customer

__author__ = "tanmay.datta86@gmail.com"
logger = logging.getLogger(__name__)


class MerchantItems(object):
    """
    Helper Class for creating merchant items
    """
    def __init__(self, itemJson):
        self.id = itemJson["id"]
        self.user_id = itemJson["user_id"]
        self.merchant_id = itemJson["merchant_id"]


class Merchant():
    """
    Class to maintain merchant object easily

    """
    def __init__(self, api_key, request, customer):
        self.api_key = api_key
        self.request = request

    def __repr__(self):
        if self.enable_full_description:
            return """
                "merchant_id": {mid},
                "company": {company} ,
                "email": {email} ,
                "name": {name} ,
                "ach allowed?": {allow_ach} ,
                "created at": {created_at} ,
                """.format(mid=self.id,
                           company=self.company,
                           email=self.email,
                           name=self.name,
                           allow_ach=self.allow_ach,
                           created_at=self.created_at)
        else:
            return """
                "merchant_id": {mid},
                "company": {company} ,
                """.format(company=self.company
                           if self.company is not None else "Not set",
                           mid=self.id)

    def update_merchant_info(self, name=None):
        """
        Call fattmerchant api and gets all the merchant info
        """
        endpoint = "merchant/?company_name={}".format(name)
        response = json.loads(self.request.get(endpoint=endpoint))

        try:
            logger.debug(response)
            merchant_info = response[u'data'][0]
            self.company = merchant_info[u'company_name']
            self.id = merchant_info[u'id']
            self.email = merchant_info[u'contact_email']
            self.name = response[u'user'][u'name']
            self.allow_ach = merchant_info[u'allow_ach']
            self.created_at = merchant_info[u'created_at']
            self.updated_at = merchant_info[u'updated_at']
            self.enable_full_description = True
        except:
            self.company = None
            self.name = None
            self.enable_full_description = False
            logger.error(
                "unable to set/find merchant info.. is api key correct ?")

    def create(self, name=None):
        """
        Can be used to create merchant if the api key is good
        """
        if name is None:
            return "Merchant name should be provided, call as .create(<name>)"

        endpoint = "merchant"
        body = {
            "name": self.name,
            "company": self.company,
            "api_key": self.api_key
        }
        id_info = self.request.put(endpoint=endpoint, payload=body)
        logger.debug("id info is {}".format(id_info))
        # set id here
        return self.id

    def items(self):
        """
        Shows all the items that merchant has in store. 
        """
        endpoint = "item"
        answer = json.loads(self.request.get(endpoint=endpoint))
        logger.debug(answer)
        items = answer["data"]
        self.merchant_items = []
        for item in items:
            logger.debug(item)
            self.merchant_items.append(MerchantItems(item))
        return self.merchant_items

    def get_all_customers(self):
        """

        Get all the customers for the merchant

        :return: list of all customers
        :rtype: list()

        """
        endpoint = "customer"
        answer = json.loads(self.request.get(endpoint=endpoint))
        self.customers = [] if self.customers is None else self.customers
        try:
            for customer in answer["data"]:
                next_customer = Customer(customer, self.id)
                next_customer.payment_methods = self.customer.payment_methods(
                    next_customer.id)
                self.customers.append(next_customer)
            return self.customers
        except Exception, e:
            logger.error("exeption happend {}".format(e))
            return None

    def charge_customer_on_token(self, customer_id, token_id, data):
        """

        Works exactly like charge  customer tokenized function but 
        do not check for the existence of customer and needs a token id

        :return: answer from the fattmerchant API
        :rtype: dict()

        """
        endpoint = "charge"
        # todo: check if the customer exiss

        payment_method_id = token_id
        logger.info("id returned by call =====> {}".format(payment_method_id))
        body = {
            "payment_method_id": payment_method_id,
            "meta": data["meta"],
            "total": data["total"],
            "pre_auth": data["pre_auth"]
        }
        answer = self.request.post(endpoint=endpoint, payload=body)
        logger.debug(json.loads(answer))
        return json.loads(answer)

    def charge_customer_tokenized(self, customer_id, data):
        """

        Charge a customer for merchant. 
        ***requires a data dictionary with following mandatory keys***
        - meta
        - total and
        - pre_auth

        the example structure for meta is 

        .. code-block:: python

            "meta": {
                "tax":2,
                "subtotal":10
                "lineItems": [{
                    "id": "optional-fm-catalog-item-id"
                    "item":"Demo Item",
                    "details":"this is a regular demo item",
                    "quantity":10,
                    "price": .1
                    }]
                },

        .. note::

            "total" is the amount you need to charge the customer

        :return: answer from the fattmerchant API
        :rtype: dict()

        """
        charge_to_customer = None
        endpoint = "charge"
        self.get_all_customers()
        logger.debug(self.customers)
        for customer in self.customers:
            if customer_id == customer.id:
                charge_to_customer = customer
        if charge_to_customer is None:
            logger.error("unable to find customer for the merchant")
            return False
        else:
            payment_method_id = charge_to_customer.payment_methods[0][u'id']
            logger.info(
                "id returned by call =====> {}".format(payment_method_id))
            body = {
                "payment_method_id": payment_method_id,
                "meta": data["meta"],
                "total": data["total"],
                "pre_auth": data["pre_auth"]
            }
            answer = self.request.post(endpoint=endpoint, payload=body)
            logger.debug(json.loads(answer))
            return json.loads(answer)

    def add_customer(self, customer):
        """

        Add a new customer for a merchant object

        :return: answer from the fattmerchant API
        :rtype: dict()

        """
        endpoint = "customer"
        body = customer.to_json()
        answer = json.loads(self.request.post(endpoint=endpoint, payload=body))
        logger.info(answer)
        return answer

    def get_all_invoices(self):
        """
        Gets all the invoices to customer by a merchant

        :return: all invoices from the fattmerchant API
        :rtype: dict()

        """
        endpoint = "invoice"
        answer = json.loads(self.request.get(endpoint=endpoint))
        return answer

    def get_items_by_code(self):
        """

        Gets a particular item specified by the code

        """
        endpoint = "item/code"
        return json.loads(self.request.get(endpoint=endpoint))

    def set_merchant_id(self, id):
        """

        .. warning::
            Anti pattern here but just it is here to make sure
            we can test the library.

        Sets the merchant id, Required in case we are getting
        merchant info from some other source and want to use
        fattmerchant client to interact with api 
        """
        self.id = id

    def team_create(self, team_info):
        """
        This call makes a new merchant team.

        .. note::
            Authentication Token Required
        
        Arguments:
            team_info {dict} -- a dictionary with team info
        
        example

        .. code-block:: JSON

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

        """
        endpoint = "team"
        answer = self.request.post(endpoint=endpoint, payload=team_info)
        logger.debug(json.loads(answer))
        return json.loads(answer)

    def team_edit_info(self, team_info):
        """
        This function allows a user to edit the information,
        such as address and name, of a merchant team.
        This only works for team members with admin as their team_role.
        This call does not change team member information.
        
        Arguments:
            team_info {dict} -- team_info json/dict object

        example

        .. code-block:: JSON

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

        .. note::
            Authentication Token and Team Admin Status Required

        """
        endpoint = "team"
        answer = self.request.put(endpoint=endpoint, payload=team_info)
        logger.debug(json.loads(answer))
        return json.loads(answer)

    def team_edit_branding_info(self, branding_info):
        """somethign
        
        .. note::
            Authentication Token and Team Admin Status Required
        
        This resource gives merchant admins the ability to change their company's branding.
        branding may be uploaded as either a PNG or JPEG image file.
        A merchant's branding will appear anywhere a merchant's object is returned.
        The merchant branding will be securely hosted on Amazon S3 bucket and recorded in our database.

        Arguments:
            branding_info {dict} -- [description]

        example

        .. code-block:: JSON

            {
                "name": "Mercedes-Benz",
                "image": "logo.png"
            }

        """
        endpoint = "team/option/branding"
        answer = self.request.put(endpoint=endpoint, payload=branding_info)
        logger.debug(json.loads(answer))
        return json.loads(answer)

    def team_list_members(self):
        """
        .. note::
            Authentication Token and Team Admin Status Required
        
        Retrieves all the users on a merchants's team, showing team-oriented details and team_role.
        Used for finding all members of a team and listing them by roles.
        """
        endpoint = "team/user"
        answer = self.request.get(endpoint=endpoint)
        logger.debug(json.loads(answer))
        return json.loads(answer)

    def team_create_member(self, user_info):
        """
        .. note::
            Authentication Token and Team Admin Status Required
        
        This creates a whole new user account in your merchant team.
        Automatically adds the user to the merchant team.
        Can only be used by users with team_rule of "admin".
        This is one of two ways to create a new user account; the other being POST /self.
        Requires a valid email, password and name at minimum.
        If team_role is not selected, it will default to "full".
        Used by team admins who want to add members to their merchant account who do not already have a Fattmerchant account.
       
        
        Arguments:
            user_info {[type]} -- user information in a dictionary
        
        example 

        .. code-block:: JSON

            {
            "email": "daniel+1024@fattmerchant.com",
            "password": "bottomline",
            "password_confirmation": "bottomline",
            "name": "Bob Dylan",
            "team_role": "full",
            "team_enabled": true,
            "send_verification_email": true,
            "url": "https://omni.fattmerchant.com/#/verify/"
            }
        """
        endpoint = "team/user"
        answer = self.request.put(endpoint=endpoint, payload=user_info)
        logger.debug(json.loads(answer))
        return json.loads(answer)

    def team_create_api_key_user(self, name, role):
        """creates api key 

        .. note::
            Authentication Token and Team Admin Status Required
        
        This creates a whole new user account in your merchant team which will have is_api_key = true.
        This will also return the api key value.
        
        Arguments:
            name {str} -- name for api key
            role {str} -- role of the api key user
        
        example

        .. code-block:: python

            team_create_api_key("do not delete - zapier key", "admin")

        """
        endpoint = "team/apikey"
        api_key_info = {"team_role": role, "name": name}
        answer = self.request.put(endpoint=endpoint, payload=api_key_info)
        logger.debug(json.loads(answer))
        return json.loads(answer)

    def team_list_api_keys(self):
        """lists all api keys

        .. note::
            Authentication Token and Team Admin Status Required
            
        List out all team member user records which are api keys.

        """
        endpoint = "team/apikey"
        answer = self.request.get(endpoint=endpoint)
        try:
            json_answer = json.loads(answer)
            logger.debug(json_answer)
            return json_answer
        except Exception, e:
            logger.critical("error ==> {}".format(e))
            return None

    def team_get_user_by_id(self, id):
        """user info by id
        
        .. note::
            Authentication Token and Team Admin Status Required
        
        Retrieves the team member that matches the given id.
        Deploys information on the team member, including their team_role.
        Used in conjunction with PUT /team/user/{id} to edit a team member.
        Requires team_role of admin to use.
       
        Arguments:
            id {str} -- user_id

        """
        endpoint = "team/user/{}".format(id)
        answer = self.request.get(endpoint=endpoint)
        logger.debug(json.loads(answer))
        return json.loads(answer)

    def team_update_user_by_id(self, id, user_info):
        """updates user info
        
        .. note::
            Authentication Token and Team Admin Status Required
        
        Allows team admins to change a team members information, such as role.
        Used in conjunction with GET /team/user/{id} to view a team members information.
        This can be used to remove a member from the team.
        Can only be used by members with team_role of "admin.
       
        Arguments:
            id {str} -- user_id
            user_info {dict} -- user_info

        example:

        .. code-block:: JSON

            {
                "id": "21a64e9e-3c13-4b85-9f85-67cb4fda808a",
                "system_admin": false,
                "name": "WILLIAM II KOHLS",
                "email": "daniel+1002@fattmerchant.com",
                "email_verification_sent_at": null,
                "email_verified_at": null,
                "created_at": "2017-05-15 19:31:35",
                "updated_at": "2017-05-15 19:41:53",
                "deleted_at": null,
                "gravatar": "//www.gravatar.com/avatar/4d6b3ceb5b37b610a68ef23fcbe0060b",
                "team_role": "admin",
                "team_admin": true,
                "team_enabled": true
                }

        """

        endpoint = "team/user/{}".format(id)
        answer = self.request.put(endpoint=endpoint, payload=user_info)
        logger.debug(json.loads(answer))
        return json.loads(answer)

    def team_update_settings(self, settings):
        """updates team settings

        .. note::
            Authentication Token and Team Admin Status Required
        

        Adds team options, also known as team settings, to a team.
        Saved as "options" under a team in the database.
        This doesn't affect the values of the options at all.
        Returns the results of the modified team options.
        Only members with team_role of "admin" can use this.
        Also used by hosted payments to change hosted payment options.
        
        Arguments:
            settings {dict} -- setting dictionary/json more info below
        
        Available Team Options
        
        - hosted_payments_token - Changes the hosted_payments token/URL.
        - hosted_payment_note - This changes the hosted_payments_note's page memo.
        - hosted_payments_success_note - Changes the hosted_payments_note's success message.
        - gateway - This changes the merchant's gateway.
            Currently available gateways are test and authorize_net.
            Gateways change where the user information will go through.
        - plan - Changes the merchant's plan.
                Plans are preset information chosen by a merchant to set a 
                course for their merchant account.
                Either basic, plus and premium are available.
                Each option will affect the merchant's functionality within
                the Fattmerchant system.
                Each plan may cost the merchant differently.
        - receipts_email - Add/updates emails to be given a receipt when a hosted_payment goes through.
        
        team Options For Mobile and Batch Over EMV Gateway 
        Used by the mobile app to store sensitive account information regarding the card reader and the EMV gateway.

        - mv_terminal_id - The ID for the EMV gateway.
        - mv_terminal_secret - Specific settings necessary for the card reader.
        - mv_user - transmits the user's username over the EMV gateway.
        - mv_password - transmits the user's password over the EMV gateway.
       
        example: 

        .. code-block:: JSON

            [
                {
                    "name": "hosted_payments_token",
                    "url": "http://localhost.app:5477/#/pay/",
                    "value": "BARTLE-_"
                },
                {
                    "name": "hosted_payments_success_note",
                    "value": "Success Note"
                },
                {
                    "name": "hosted_payments_note",
                    "value": "Page Memo"
                }
            ]

        """
        endpoint = "team/option"
        answer = self.request.put(endpoint=endpoint, payload=settings)
        logger.debug(json.loads(answer))
        return json.loads(answer)

    def team_update_registration_data(self, registration_data):
        pass

    def team_change_plan(self, plan):
        """changes team plan

        .. note::
            Authentication Token and Team Admin Status Required
        
        This function changes the merchant team's plan.
        Merchant teams have a plan they can set that affects the functionality of their account.
        There are two plan types: PORTAL and PREMIUM.
        Different plans have different payment options and processing.
        Plans on affects what API calls can be made.
        This can only be called by a team admin.

        Available Team Plans
        - PORTAL - has access to reporting, transactions and team in the API.
        - PREMIUM - has access to everything in the API.
        
        Arguments:
            plan {str} -- plan description --> {"portal"/"premium"}
        """
        endpoint = "team/option/plan"
        body = {"plan": plan.upper()}
        answer = self.request.put(endpoint=endpoint, payload=body)
        logger.debug(json.loads(answer))
        return json.loads(answer)

    def team_change_gateway(self, gateway):
        """Changes teams gateway
        
        .. note::
            Authentication Token and Team Admin Status Required
        
        Gateways are the pathways chosen by users to decide where they need their information to go through.
        Currently available gateways are test and authorize_net.
        This process changes the user's gateway to another one using a login and password.
        Can only be changed by team members with team_role of "admin".
        Newly created teams that haven't registered a gateway with this function will automatically have gateway_name and gateway_type set to null.
       
       

        Arguments:
            gateway {str} -- gateway string
        """
        endpoint = "team/option/gateway"
        body = {"value": gateway.upper()}
        answer = self.request.put(endpoint=endpoint, payload=body)
        logger.debug(json.loads(answer))
        return json.loads(answer)
