from datetime import datetime

from fattmerchant.models import Customer


class PaymentMethod():
    """
    Payment Method model class
    """
    def __init__(self, data):
        self.id = data.get("id")
        self.customer_id = data.get("customer_id")
        self.merchant_id = data.get("merchant_id")
        self.user_id = data.get("user_id")
        self.nickname = data.get("nickname")
        self.has_cvv = data.get("has_cvv")
        self.is_default = data.get("is_default")
        self.method = data.get("method")
        self.person_name = data.get("person_name")
        self.card_type = data.get("card_type")
        self.card_last_four = data.get("card_last_four")
        self.card_exp = data.get("card_exp")
        self.bank_name = data.get("bank_name")
        self.bank_type = data.get("bank_type")
        self.bank_holder_type = data.get("bank_holder_type")
        self.address_1 = data.get("address_1")
        self.address_2 = data.get("address_2")
        self.address_city = data.get("address_city")
        self.address_state = data.get("address_state")
        self.address_zip = data.get("address_zip")
        self.address_country = data.get("address_country")
        self.purged_at = datetime.strptime(
            data.get("purged_at"),
            '%Y-%m-%d %H:%M:%S') if data.get("purged_at") else None
        self.created_at = datetime.strptime(
            data.get("created_at"),
            '%Y-%m-%d %H:%M:%S') if data.get("created_at") else None
        self.updated_at = datetime.strptime(
            data.get("updated_at"),
            '%Y-%m-%d %H:%M:%S') if data.get("updated_at") else None
        self.deleted_at = datetime.strptime(
            data.get("deleted_at"),
            '%Y-%m-%d %H:%M:%S') if data.get("deleted_at") else None
        self.meta = data.get("meta")
        self.bin_type = data.get("bin_type")
        self.card_exp_datetime = datetime.strptime(
            data.get("card_exp_datetime"),
            '%Y-%m-%d %H:%M:%S') if data.get("card_exp_datetime") else None
        self.is_usable_in_vt = data.get("is_usable_in_vt")
        self.customer = Customer(data.get("customer")) \
            if data.get("customer") else None

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
