from datetime import datetime


class Merchant():
    """
    Merchant model class
    """
    def __init__(self, data):
        self.id = data.get("id")
        self.mid = data.get("mid")
        self.status = data.get("status")
        self.subdomain = data.get("subdomain")
        self.company_name = data.get("company_name")
        self.display_name = data.get("display_name")
        self.contact_name = data.get("contact_name")
        self.contact_email = data.get("contact_email")
        self.contact_phone = data.get("contact_phone")
        self.address_1 = data.get("address_1")
        self.address_2 = data.get("address_2")
        self.address_city = data.get("address_city")
        self.address_state = data.get("address_state")
        self.address_zip = data.get("address_zip")
        self.hosted_payments_token = data.get("hosted_payments_token")
        self.options = data.get("options")
        self.notes = data.get("notes")
        self.gateway_type = data.get("gateway_type")
        self.vendor_keys = data.get("vendor_keys")
        self.processor = data.get("processor")
        self.partner = data.get("partner")
        self.product_type = data.get("product_type")
        self.is_enterprise = data.get("is_enterprise")
        self.is_payfac = data.get("is_payfac")
        self.fm_billing_schedule_id = data.get("fm_billing_schedule_id")
        self.welcome_email_sent_at = datetime.strptime(
            data.get("welcome_email_sent_at"),
            '%Y-%m-%d %H:%M:%S') if data.get("welcome_email_sent_at") else None
        self.created_at = datetime.strptime(
            data.get("created_at"),
            '%Y-%m-%d %H:%M:%S') if data.get("created_at") else None
        self.updated_at = datetime.strptime(
            data.get("updated_at"),
            '%Y-%m-%d %H:%M:%S') if data.get("updated_at") else None
        self.deleted_at = datetime.strptime(
            data.get("deleted_at"),
            '%Y-%m-%d %H:%M:%S') if data.get("deleted_at") else None
        self.brand = data.get("brand")
        self.branding = data.get("branding")
        self.allow_ach = data.get("allow_ach")
        self.is_portal = data.get("is_portal")
        self.allow_credits = data.get("allow_credits")
        self.allow_terminal = data.get("allow_terminal")

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
