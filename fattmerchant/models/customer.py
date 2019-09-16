from datetime import datetime


class Customer():
    """
    Customer model class
    """
    def __init__(self, data):
        self.id = data.get("id")
        self.firstname = data.get("firstname")
        self.lastname = data.get("lastname")
        self.company = data.get("company")
        self.email = data.get("email")
        self.cc_emails = data.get("cc_emails")
        self.cc_sms = data.get("cc_sms")
        self.phone = data.get("phone")
        self.address_1 = data.get("address_1")
        self.address_2 = data.get("address_2")
        self.address_city = data.get("address_city")
        self.address_state = data.get("address_state")
        self.address_zip = data.get("address_zip")
        self.address_country = data.get("address_country")
        self.notes = data.get("notes")
        self.reference = data.get("reference")
        self.options = data.get("options")
        self.created_at = datetime.strptime(
            data.get("created_at"),
            '%Y-%m-%d %H:%M:%S') if data.get("created_at") else None
        self.updated_at = datetime.strptime(
            data.get("updated_at"),
            '%Y-%m-%d %H:%M:%S') if data.get("updated_at") else None
        self.deleted_at = datetime.strptime(
            data.get("deleted_at"),
            '%Y-%m-%d %H:%M:%S') if data.get("deleted_at") else None
        self.allow_invoice_credit_card_payments = data.get(
            "allow_invoice_credit_card_payments")
        self.gravatar = data.get("gravatar")

    def __repr__(self):
        repr = '{}(' \
            'id: {!r}, ' \
            'firstname: {!r}, ' \
            'lastname: {!r}, ' \
            'company: {!r}, ' \
            'email: {!r}, ' \
            'cc_emails: {!r}, ' \
            'cc_sms: {!r}, ' \
            'phone: {!r}, ' \
            'address_1: {!r}, ' \
            'address_2: {!r}, ' \
            'address_city: {!r}, ' \
            'address_state: {!r}, ' \
            'address_zip: {!r}, ' \
            'address_country: {!r}, ' \
            'notes: {!r}, ' \
            'reference: {!r}, ' \
            'options: {!r}, ' \
            'created_at: {!r}, ' \
            'updated_at: {!r}, ' \
            'deleted_at: {!r}, ' \
            'allow_invoice_credit_card_payments: {!r}, ' \
            'gravatar: {!r})'.format(
                self.__class__.__name__,
                self.id,
                self.firstname,
                self.lastname,
                self.company,
                self.email,
                self.cc_emails,
                self.cc_sms,
                self.phone,
                self.address_1,
                self.address_2,
                self.address_city,
                self.address_state,
                self.address_zip,
                self.address_country,
                self.notes,
                self.reference,
                self.options,
                self.created_at,
                self.updated_at,
                self.deleted_at,
                self.allow_invoice_credit_card_payments,
                self.gravatar
            )

        return repr
