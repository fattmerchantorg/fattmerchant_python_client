import requests
import os
import logging
import json

from fattmerchant.exceptions import FattmerchantException, \
    InvalidTokenException, ResourceDoesNotExistException, \
    DuplicateResourceException, InvalidRequestDataException

self_path = os.path.dirname(__file__)
logger = logging.getLogger(__name__)


class Request(object):
    """
    Class to get a valid fattmerchant request format

    """
    def __init__(self, api_key, env="prod"):
        self.api_key = api_key
        self.use_env(env)

    def use_env(self, env):
        """
        change enviornment for testing

        :param env: string of enviornment can be "local", "demo" or "prod"

        """

        prod_url = 'https://apiprod.fattlabs.com'
        prod_fq_url = 'https://apiprod.fattlabs.com/query'
        demo_url = 'https://apidemo.fattlabs.com'
        demo_fq_url = 'https://apidemo.fattlabs.com/query'
        local_url = 'http://localhost:8000'
        local_fq_url = 'http://localhost:3005'

        self.env = env
        self.api = {}

        if (env == "prod"):
            self.api["core"] = prod_url
            self.api["fq"] = prod_fq_url
        elif (env == "demo"):
            self.api["core"] = demo_url
            self.api["fq"] = demo_fq_url
        elif (env == "local"):
            self.api["core"] = local_url
            self.api["fq"] = local_fq_url

    def __make_request(
        self, api_type, method, endpoint, options={}, payload=None
    ):
        url = "{api}/{endpoint}{query_string}".format(
            api=self.api[api_type],
            endpoint=endpoint,
            query_string=self.__build_query_string(options)
        )

        headers = self.__build_headers()

        # Get the correct "requests" class method by passing
        # in the request method that we want
        req = getattr(requests, method, 'get')

        if payload is not None:
            res = req(url, headers=headers, data=json.dumps(payload))
        else:
            res = req(url, headers=headers)

        if res.status_code == 200:
            return res.text

        msg = "ERROR occured while trying to send a {} request: " \
            "URL: {}, HEADERS: {}, PAYLOAD: {} " \
            "STATUS CODE: {}, RESPONSE: {}"

        logger.error(
            msg.format(
                method.upper(), url, headers, payload, res.status_code,
                res.text
            )
        )

        if res.status_code == 401:
            raise InvalidTokenException(message=res.text)
        elif res.status_code == 404:
            raise ResourceDoesNotExistException(message=res.text)
        elif res.status_code == 409:
            raise DuplicateResourceException(message=res.text)
        elif res.status_code == 400:
            raise InvalidRequestDataException(
                status_code=400, message=res.text
            )
        elif res.status_code == 422:
            raise InvalidRequestDataException(message=res.text)
        else:
            raise FattmerchantException(message=res.text)

    def __build_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {api_key}'.format(api_key=self.api_key),
            'Accept': 'application/json'
        }

    def __build_query_string(self, params):
        if (len(params) == 0):
            return ""

        query_strings = []

        for key, value in params.items():
            query_strings.append("{}={}".format(key, value))

        return "?{}".format("&".join(query_strings))

    def get(self, api='core', endpoint='', options={}):
        """
        Calls respective api with a `GET` HTTP method

        :param str api: Fattmerchant API base url to be requested
        :param str endpoint: API endpoint to be requested
        """
        return self.__make_request(api, 'get', endpoint, options=options)

    def post(self, api='core', endpoint='', payload={}):
        """
        Calls respective api with a `POST` HTTP method

        :param str api: Fattmerchant API base url to be requested
        :param str endpoint: API endpoint to be requested
        :param dict payload: Data to be sent along with API request
        """
        return self.__make_request(api, 'post', endpoint, payload=payload)

    def put(self, api='core', endpoint='', payload={}):
        """
        Calls respective api with a `PUT` HTTP method

        :param str api: Fattmerchant API base url to be requested
        :param str endpoint: API endpoint to be requested
        :param dict payload: Data to be sent along with API request
        """
        return self.__make_request(api, 'put', endpoint, payload=payload)
