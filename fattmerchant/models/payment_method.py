from datetime import datetime

from fattmerchant.models import Customer


class PaymentMethod(object):
    """
    Payment Method model class
    """
    def __init__(self, data):
        self.id = data.get("id")
        """ Id of the payment method """

        self.customer_id = data.get("customer_id")
        """ Id of customer the payment method belongs to """

        self.merchant_id = data.get("merchant_id")
        """ Id of merchant the payment method belongs to """

        self.user_id = data.get("user_id")
        """ Id of user the payment method belongs to """

        self.nickname = data.get("nickname")
        """ Nickname of the payment method """

        self.has_cvv = data.get("has_cvv")
        """ Whether the payment method has a cvv or not """

        self.is_default = data.get("is_default")
        """ Whether the payment method is the default or not """

        self.method = data.get("method")
        """ The type of payment method """

        self.person_name = data.get("person_name")
        """ The name on a credit card payment method """

        self.card_type = data.get("card_type")
        """ The type of a credit card payment method """

        self.card_last_four = data.get("card_last_four")
        """ The last four numbers on a credit card payment method """

        self.card_exp = data.get("card_exp")
        """ The expiration date on a credit card payment method """

        self.bank_name = data.get("bank_name")
        """ The bank name on an ACH payment method """

        self.bank_type = data.get("bank_type")
        """ The bank type on an ACH payment method """

        self.bank_holder_type = data.get("bank_holder_type")
        """ The bank holder type on an ACH payment method """

        self.address_1 = data.get("address_1")
        """ The address for the payment method """

        self.address_2 = data.get("address_2")
        """ The address additional details for the payment method """

        self.address_city = data.get("address_city")
        """ The address city for the payment method """

        self.address_state = data.get("address_state")
        """ The address state for the payment method """

        self.address_zip = data.get("address_zip")
        """ The address zip for the payment method """

        self.address_country = data.get("address_country")
        """ The address country for the payment method """

        self.purged_at = datetime.strptime(
            data.get("purged_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("purged_at") else None
        """ When the payment method was purged """

        self.created_at = datetime.strptime(
            data.get("created_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("created_at") else None
        """ When the payment method was created """

        self.updated_at = datetime.strptime(
            data.get("updated_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("updated_at") else None
        """ When the payment method was updated """

        self.deleted_at = datetime.strptime(
            data.get("deleted_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("deleted_at") else None
        """ When the payment method was deleted """

        self.meta = data.get("meta")
        """ Any meta data for the payment method """

        self.bin_type = data.get("bin_type")
        """ The bank name on an ACH payment method """

        self.card_exp_datetime = datetime.strptime(
            data.get("card_exp_datetime"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("card_exp_datetime") else None
        """ The the expiry date/time of the credit card """

        self.is_usable_in_vt = data.get("is_usable_in_vt")
        """ Whether or not the payment method is usable in Omni """

        self.customer = Customer(data.get("customer")) \
            if data.get("customer") else None
        """ The customer for the payment method """
    def __repr__(self):
        repr = '{}(' \
            'id: {!r}, ' \
            'customer_id: {!r}, ' \
            'merchant_id: {!r}, ' \
            'user_id: {!r}, ' \
            'nickname: {!r}, ' \
            'has_cvv: {!r}, ' \
            'is_default: {!r}, ' \
            'method: {!r}, ' \
            'person_name: {!r}, ' \
            'card_type: {!r}, ' \
            'card_last_four: {!r}, ' \
            'card_exp: {!r}, ' \
            'bank_name: {!r}, ' \
            'bank_type: {!r}, ' \
            'bank_holder_type: {!r}, ' \
            'address_1: {!r}, ' \
            'address_2: {!r}, ' \
            'address_city: {!r}, ' \
            'address_state: {!r}, ' \
            'address_zip: {!r}, ' \
            'address_country: {!r}, ' \
            'purged_at: {!r}, ' \
            'deleted_at: {!r}, ' \
            'created_at: {!r}, ' \
            'updated_at: {!r}, ' \
            'meta: {!r}, ' \
            'bin_type: {!r}, ' \
            'card_exp_datetime: {!r}, ' \
            'is_usable_in_vt: {!r}, ' \
            'customer: {!r})'.format(
                self.__class__.__name__,
                self.id,
                self.customer_id,
                self.merchant_id,
                self.user_id,
                self.nickname,
                self.has_cvv,
                self.is_default,
                self.method,
                self.person_name,
                self.card_type,
                self.card_last_four,
                self.card_exp,
                self.bank_name,
                self.bank_type,
                self.bank_holder_type,
                self.address_1,
                self.address_2,
                self.address_city,
                self.address_state,
                self.address_zip,
                self.address_country,
                self.purged_at,
                self.deleted_at,
                self.created_at,
                self.updated_at,
                self.meta,
                self.bin_type,
                self.card_exp_datetime,
                self.is_usable_in_vt,
                self.customer,
            )

        return repr
