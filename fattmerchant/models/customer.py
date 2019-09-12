import logging

logger = logging.getLogger(__name__)


class Customer(object):
    """
    The customer object given by the fatterchant api
    """
    def __init__(self, customer_info, merchant_id=None):
        """
        try to initiate a customer object with sane defaults
        """
        self.merchant_id = merchant_id
        self.id = customer_info.get("id", None)
        self.firstname = customer_info.get("firstname", None)
        self.lastname = customer_info.get("lastname", None)
        self.company = customer_info.get("company", None)
        self.email = customer_info.get("email", None)
        try:
            cc_email = customer_info.get("cc_emails", "[]")
            if cc_email in [None, []]:
                self.cc_emails = []
            else:
                self.cc_emails = eval(cc_email)
        except Exception:
            logger.error("wrong cc emails got {}".format(
                customer_info["cc_emails"]))
            self.cc_emails = list()
        self.phone = customer_info.get("phone", None)
        self.address_1 = customer_info.get("address_1", None)
        self.address_2 = customer_info.get("address_2", None)
        self.address_city = customer_info.get("address_city", None)
        self.address_state = customer_info.get("address_state", None)
        self.address_zip = customer_info.get("address_zip", None)
        self.address_country = customer_info.get("address_country", None)
        self.notes = customer_info.get("notes", None)
        self.reference = customer_info.get("reference", None)
        self.options = customer_info.get("options", None)
        self.created_at = customer_info.get("created_at", None)
        self.updated_at = customer_info.get("updated_at", None)
        self.deleted_at = customer_info.get("deleted_at", None)
        self.gravatar = customer_info.get("gravatar", None)
        self.payment_methods = list()

    def update_payment_methods_for(self, payment_methods):
        """
        Find all payment methods for a given customer

        """
        self.payment_methods = payment_methods

    def to_json(self):
        """
        Json representation that can be used for the API
        """
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "company": self.company,
            "email": self.email,
            "cc_emails": self.cc_emails,
            "phone": self.phone,
            "address_1": self.address_1,
            "address_2": self.address_2,
            "address_city": self.address_city,
            "address_state": self.address_state,
            "address_zip": unicode(self.address_zip),
            "address_country": self.address_country,
            "reference": self.reference
        }

    def __repr__(self):
        return """
            "first name": {fname},
            "last name": {lname},
            "email": {email},
            """.format(
            fname=self.firstname,
            lname=self.lastname,
            email=self.email,
        )
