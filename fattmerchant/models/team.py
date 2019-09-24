from datetime import datetime


class Team(object):
    """
    Team model class
    """
    def __init__(self, data):
        self.id = data.get("id")
        """ Id of the team """

        self.mid = data.get("mid")
        """ Id assigned to team via gateway """

        self.status = data.get("status")
        """ Status of the team """

        self.subdomain = data.get("subdomain")
        """ Subdomain for the team """

        self.company_name = data.get("company_name")
        """ Company name of the team """

        self.display_name = data.get("display_name")
        """ Display name for the team """

        self.contact_name = data.get("contact_name")
        """ Contact name for the team """

        self.contact_email = data.get("contact_email")
        """ Contact email for the team """

        self.contact_phone = data.get("contact_phone")
        """ Contact phone for the team """

        self.address_1 = data.get("address_1")
        """ Main address of the team """

        self.address_2 = data.get("address_2")
        """ Additional address details of the team """

        self.address_city = data.get("address_city")
        """ Address city for the team """

        self.address_state = data.get("address_state")
        """ Address state for the team """

        self.address_zip = data.get("address_zip")
        """ Address zip for the team """

        self.hosted_payments_token = data.get("hosted_payments_token")
        """ All hosted payment methods for the team """

        self.plan = data.get("plan")
        """ Plan team has signed up for """

        self.options = data.get("options"),
        """ All options for the team """

        self.gateway_type = data.get("gateway_type")
        """ Gateway type of the team (deprecated) """

        self.processor = data.get("processor")
        """ Payment processor of the team """

        self.partner = data.get("partner")
        """ Optional tracking field of where the team came from """

        self.product_type = data.get("product_type")
        """ Tracking field for which product the team is using """

        self.is_enterprise = data.get("is_enterprise")
        """ Whether the team is an enterprise team or not """

        self.is_payfac = data.get("is_payfac")
        """ Whether the team is a payfac team """

        self.fm_billing_schedule_id = data.get("fm_billing_schedule_id")
        """ Schedule id for when the team is to be billed """

        self.welcome_email_sent_at = datetime.strptime(
            data.get("welcome_email_sent_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("welcome_email_sent_at") else None
        """ When the welcome email was sent """

        self.created_at = datetime.strptime(
            data.get("created_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("created_at") else None
        """ When the team was created """

        self.updated_at = datetime.strptime(
            data.get("updated_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("updated_at") else None
        """ When the team was updated """

        self.deleted_at = datetime.strptime(
            data.get("deleted_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("deleted_at") else None
        """ When the team was deleted """

        self.brand = data.get("brand")
        """ Brand of the team """

        self.branding = data.get("branding")
        """ The logo for the team """

        self.allow_ach = data.get("allow_ach")
        """ Whether to allow ACH transactions """

        self.is_portal = data.get("is_portal")
        """ Whether the team is a portal team or not """

        self.allow_credits = data.get("allow_credits")
        """ Whether credits are allowed for this team or not """

        self.allow_terminal = data.get("allow_terminal")
        """ Whether the team is able to process terminal transactions """
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
