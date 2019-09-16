from fattmerchant.request import Request
from fattmerchant.controllers import TransactionsController, \
    CustomersController, ChargesController, TeamsController, \
    DepositsController


class FMClient(object):
    """
    Class to set up the Fattmerchant Python SDK
    """
    def __init__(self, api_key, env="prod"):
        request = Request(api_key, env)

        self.customers = CustomersController(request)
        self.teams = TeamsController(request)
        self.transactions = TransactionsController(request)
        self.deposits = DepositsController(request)
        self.charges = ChargesController(request)
