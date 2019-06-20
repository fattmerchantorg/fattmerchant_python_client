"Helper class for creating fattmerchant requests"

import requests

class FMRequest():
    "Call to get valid fattmerchant request"
    fm_link = r'https://apiprod.fattlabs.com'
    api_key_default = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZXJjaGFudCI6ImYzMjJlZWM4LTVhYzYtNGZhZS04YzI3LTAwZjUyZTFiN2JkMyIsImdvZFVzZXIiOmZhbHNlLCJzdWIiOiIzNzZiMDVkZC05ZDY3LTRmMzMtODVmOS05OTNmY2RhN2QxZmMiLCJpc3MiOiJodHRwOi8vYXBpZGVtby5mYXR0bGFicy5jb20vdGVhbS9hcGlrZXkiLCJpYXQiOjE1NTg2MTYxODgsImV4cCI6NDcxMjIxNjE4OCwibmJmIjoxNTU4NjE2MTg4LCJqdGkiOiJQYWZYeDNTcEpDaEJ1Ym42IiwiYXNzdW1pbmciOmZhbHNlfQ.mZE4X0cJLjBpyfo4Wts16Wk4bOn3_MadLfYTNwX57jg'
    def __init__(self):
        self.header = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {api_key}',
                       'Accept': 'application/json'}
        self.body = None
        self.api_key = None

    def get_request(self, endpoint: str, body=None):
        url = self.fm_link + "/" + endpoint
        self.body = body
        self.api_key = self.api_key_default if self.api_key is None else self.api_key
        self.update_header()
        if self.body is not None:
            req = requests.get(url, headers=self.header, data=self.body)
        else:
            req = requests.get(url, headers=self.header)
        return req.text
    
    def put_request(self, endpoint: str, body=None):
        url = self.fm_link + "/" + endpoint
        self.body = body
        self.api_key = self.api_key_default if self.api_key is None else self.api_key
        self.update_header()
        if self.body is not None:
            req = requests.put(url, headers=self.header, data=self.body)
        else:
            req = requests.put(url, headers=self.header)
        return req.text

    def post_request(self, endpoint: str, body=None):
        url = self.fm_link + "/" + endpoint
        self.body = body
        self.api_key = self.api_key_default if self.api_key is None else self.api_key
        self.update_header()
        if self.body is not None:
            req = requests.post(url, headers=self.header, data=self.body)
        else:
            req = requests.post(url, headers=self.header)
        return req.text

    def set_api_key(self, key):
        self.api_key = key
    
    def update_header(self):
        self.header['Authorization'] = self.header['Authorization'].format(api_key = api_key)


