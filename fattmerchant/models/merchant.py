from datetime import datetime


class Merchant(object):
    """
    Merchant model class
    """ 
    def __init__(self, data):
        self.id = data.get("id")
        """ Id of the merchant """

        self.mid = data.get("mid")
        """ Id assigned to merchant via gateway """

        self.status = data.get("status")
        """ Status of the merchant """

        self.subdomain = data.get("subdomain")
        """ Subdomain of the merchant """

        self.company_name = data.get("company_name")
        """ Company name of the merchant """

        self.display_name = data.get("display_name")
        """ Display name of the merchant """

        self.contact_name = data.get("contact_name")
        """ Contact name of the merchant """

        self.contact_email = data.get("contact_email")
        """ Contact email of the merchant """

        self.contact_phone = data.get("contact_phone")
        """ Contact phone of the merchant """

        self.address_1 = data.get("address_1")
        """ Address of the merchant """

        self.address_2 = data.get("address_2")
        """ Address additional details of the merchant """

        self.address_city = data.get("address_city")
        """ City for the address of the merchant """

        self.address_state = data.get("address_state")
        """ State for the address of the merchant """

        self.address_zip = data.get("address_zip")
        """ Zip code for the address of the merchant """

        self.hosted_payments_token = data.get("hosted_payments_token")
        """ Country for the address of the merchant """

        self.options = data.get("options")
        """ Optional metadata in JSON format about the merchant """

        self.notes = data.get("notes")
        """ Any notes about the merchant """

        self.gateway_type = data.get("gateway_type")
        """ Gateway type of the merchant (deprecated) """

        self.vendor_keys = data.get("vendor_keys")
        """ Vendor keys for the merchant """

        self.processor = data.get("processor")
        """ Payment processor of the merchant """

        self.partner = data.get("partner")
        """ Optional tracking field of where the merchant came from """

        self.product_type = data.get("product_type")
        """ Tracking field for which product the merchant is using """

        self.is_enterprise = data.get("is_enterprise")
        """ Whether the merchant is an enterprise merchant or not """

        self.is_payfac = data.get("is_payfac")
        """ Whether the merchant is a payfac merchant """

        self.fm_billing_schedule_id = data.get("fm_billing_schedule_id")
        """ Schedule id for when the merchant is to be billed """

        self.welcome_email_sent_at = datetime.strptime(
            data.get("welcome_email_sent_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("welcome_email_sent_at") else None
        """ When the welcome email was sent """

        self.created_at = datetime.strptime(
            data.get("created_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("created_at") else None
        """ When the customer was created """

        self.updated_at = datetime.strptime(
            data.get("updated_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("updated_at") else None
        """ The last time the customer was updated """

        self.deleted_at = datetime.strptime(
            data.get("deleted_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("deleted_at") else None
        """ When the customer was deleted """

        self.brand = data.get("brand")
        """ Brand of the merchant """

        self.branding = data.get("branding")
        """ The logo for the merchant """

        self.allow_ach = data.get("allow_ach")
        """ Whether to allow ACH transactions """

        self.is_portal = data.get("is_portal")
        """ Whether the merchant is a portal merchant or not """

        self.allow_credits = data.get("allow_credits")
        """ Whether credits are allowed for this merchant or not """

        self.allow_terminal = data.get("allow_terminal")
        """ Whether the merchant is able to process terminal transactions """
    def __repr__(self):
        repr = '{}(' \
            'id: {!r}, ' \
            'mid: {!r}, ' \
            'status: {!r}, ' \
            'subdomain: {!r}, ' \
            'company_name: {!r}, ' \
            'display_name: {!r}, ' \
            'contact_name: {!r}, ' \
            'contact_email: {!r}, ' \
            'contact_phone: {!r}, ' \
            'address_1: {!r}, ' \
            'address_2: {!r}, ' \
            'address_city: {!r}, ' \
            'address_state: {!r}, ' \
            'address_zip: {!r}, ' \
            'hosted_payments_token: {!r}, ' \
            'options: {!r}, ' \
            'notes: {!r}, ' \
            'gateway_type: {!r}, ' \
            'vendor_keys: {!r}, ' \
            'processor: {!r}, ' \
            'partner: {!r}, ' \
            'product_type: {!r}, ' \
            'is_enterprise: {!r}, ' \
            'is_payfac: {!r}, ' \
            'fm_billing_schedule_id: {!r}, ' \
            'welcome_email_sent_at: {!r}, ' \
            'created_at: {!r}, ' \
            'updated_at: {!r}, ' \
            'deleted_at: {!r}, ' \
            'brand: {!r}, ' \
            'branding: {!r}, ' \
            'allow_ach: {!r}, ' \
            'is_portal: {!r}, ' \
            'allow_credits: {!r}, ' \
            'allow_terminal: {!r})'.format(
                self.__class__.__name__,
                self.id,
                self.mid,
                self.status,
                self.subdomain,
                self.company_name,
                self.display_name,
                self.contact_name,
                self.contact_email,
                self.contact_phone,
                self.address_1,
                self.address_2,
                self.address_city,
                self.address_state,
                self.address_zip,
                self.hosted_payments_token,
                self.options,
                self.notes,
                self.gateway_type,
                self.vendor_keys,
                self.processor,
                self.partner,
                self.product_type,
                self.is_enterprise,
                self.is_payfac,
                self.fm_billing_schedule_id,
                self.welcome_email_sent_at,
                self.created_at,
                self.updated_at,
                self.deleted_at,
                self.brand,
                self.branding,
                self.allow_ach,
                self.is_portal,
                self.allow_credits,
                self.allow_terminal
            )

        return repr
