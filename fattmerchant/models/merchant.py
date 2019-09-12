class Merchant(object):
    """
    Helper Class for creating merchant items
    """
    def __init__(self, itemJson):
        self.id = itemJson["id"]
        self.user_id = itemJson["user_id"]
        self.merchant_id = itemJson["merchant_id"]