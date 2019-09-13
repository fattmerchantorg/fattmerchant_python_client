class Team():
    """
    Team model class
    """
    def __init__(self, data):
        self.id = data.get("id", None)
        self.mid = data.get("mid", None)
        self.status = data.get("status", None)
        self.subdomain = data.get("subdomain", None)
        self.company_name = data.get("company_name", None)
        self.display_name = data.get("display_name", None)
        self.contact_name = data.get("contact_name", None)
        self.contact_email = data.get("contact_email", None)
        self.contact_phone = data.get("contact_phone", None)
        self.address_1 = data.get("address_1", None)
        self.address_2 = data.get("address_2", None)
        self.address_city = data.get("address_city", None)
        self.address_state = data.get("address_state", None)
        self.address_zip = data.get("address_zip", None)
        self.hosted_payments_token = data.get("hosted_payments_token", None)
        self.plan = data.get("plan", None)
        self.options = data.get("options", None),
        self.gateway_type = data.get("gateway_type", None)
        self.processor = data.get("processor", None)
        self.partner = data.get("partner", None)
        self.product_type = data.get("product_type", None)
        self.is_enterprise = data.get("is_enterprise", None)
        self.is_payfac = data.get("is_payfac", None)
        self.fm_billing_schedule_id = data.get("fm_billing_schedule_id", None)
        self.welcome_email_sent_at = data.get("welcome_email_sent_at", None)
        self.created_at = data.get("created_at", None)
        self.updated_at = data.get("updated_at", None)
        self.deleted_at = data.get("deleted_at", None)
        self.brand = data.get("brand", None)
        self.branding = data.get("branding", None)
        self.allow_ach = data.get("allow_ach", None)
        self.is_portal = data.get("is_portal", None)
        self.allow_credits = data.get("allow_credits", None)
        self.allow_terminal = data.get("allow_terminal", None)

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
            'plan: {!r}, ' \
            'options: {!r}, ' \
            'gateway_type: {!r}, ' \
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
                self.plan,
                self.options,
                self.gateway_type,
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
