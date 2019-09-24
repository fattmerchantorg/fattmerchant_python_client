from datetime import datetime


class Customer(object):
    """
    Customer model class
    """
    def __init__(self, data):
        self.id = data.get("id")
        """ Id of the customer """

        self.firstname = data.get("firstname")
        """ First name of the customer """

        self.lastname = data.get("lastname")
        """ Last name of the customer """

        self.company = data.get("company")
        """ Company of the customer """

        self.email = data.get("email")
        """ Email of the customer """

        self.cc_emails = data.get("cc_emails")
        """
        Extra email addresses all emails will also be sent to
        for customer receipts or invoices
        """

        self.cc_sms = data.get("cc_sms")
        """
        Extra phone numbers all texts will also be sent to
        for customer receipts or invoices
        """

        self.phone = data.get("phone")
        """ Phone number of the customer """

        self.address_1 = data.get("address_1")
        """ Address of the customer """

        self.address_2 = data.get("address_2")
        """ Address additional details of the customer """

        self.address_city = data.get("address_city")
        """ City for the address of the customer """

        self.address_state = data.get("address_state")
        """ State for the address of the customer """

        self.address_zip = data.get("address_zip")
        """ Zip code for the address of the customer """

        self.address_country = data.get("address_country")
        """ Country for the address of the customer """

        self.notes = data.get("notes")
        """ Any notes about the customer """

        self.reference = data.get("reference")
        """ Customizable name to reference customer """

        self.options = data.get("options")
        """ Optional metadata in JSON format about the customer """

        self.created_at = datetime.strptime(
            data.get("created_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("created_at") else None
        """ When the customer was created """

        self.updated_at = datetime.strptime(
            data.get("updated_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("updated_at") else None
        """ When the customer was updated """

        self.deleted_at = datetime.strptime(
            data.get("deleted_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("deleted_at") else None
        """ When the customer was deleted """

        self.allow_invoice_credit_card_payments = data.get(
            "allow_invoice_credit_card_payments"
        )
        """ Whether to allow credit card payments for customer on invoices """

        self.gravatar = data.get("gravatar")
        """ Gravatar of the customer """
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
