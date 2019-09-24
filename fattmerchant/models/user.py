from datetime import datetime


class User(object):
    """
    User model class
    """
    def __init__(self, data):
        self.id = data.get("id")
        """ Id of the user """

        self.system_admin = data.get("system_admin")
        """ Whether the user is a system admin or not """

        self.name = data.get("name")
        """ Name of the user """

        self.email = data.get("email")
        """ Email of the user """

        self.email_verification_sent_at = datetime.strptime(
            data.get("email_verification_sent_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("email_verification_sent_at") else None
        """ When the verification email was sent """

        self.email_verified_at = datetime.strptime(
            data.get("email_verified_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("email_verified_at") else None
        """ When the email was verified """

        self.is_api_key = data.get("is_api_key")
        """ Whether this user is an api key or not """

        self.acknowledgments = data.get("acknowledgments")
        """ Any acknowledgments for the user """

        self.created_at = datetime.strptime(
            data.get("created_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("created_at") else None
        """ When the user was created """

        self.updated_at = datetime.strptime(
            data.get("updated_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("updated_at") else None
        """ When the user was updated """

        self.deleted_at = datetime.strptime(
            data.get("deleted_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("deleted_at") else None
        """ When the user was deleted """

        self.brand = data.get("brand")
        """ Brand of the user """

        self.gravatar = data.get("gravatar")
        """ Gravatar of the user """

        self.team_admin = data.get("team_admin")
        """ Whether the user is a team admin or now """

        self.team_enabled = data.get("team_enabled")
        """ Whether or not this user is enabled for a team  """

        self.team_role = data.get("team_role")
        """ The role this user has on the associated team """

        self.merchant_options = data.get("merchant_options")
        """ Settings for the user for a merchant """

        self.is_default = data.get("is_default")
        """ Default merchant to load when user logs in to Omni """
    def __repr__(self):
        repr = '{}(' \
            'id: {!r}, ' \
            'system_admin: {!r}, ' \
            'name: {!r}, ' \
            'email: {!r}, ' \
            'email_verification_sent_at: {!r}, ' \
            'email_verified_at: {!r}, ' \
            'is_api_key: {!r}, ' \
            'acknowledgments: {!r}, ' \
            'created_at: {!r}, ' \
            'updated_at: {!r}, ' \
            'deleted_at: {!r}, ' \
            'brand: {!r}, ' \
            'gravatar: {!r}, ' \
            'team_admin: {!r}, ' \
            'team_enabled: {!r}, ' \
            'team_role: {!r}, ' \
            'merchant_options: {!r}, ' \
            'is_default: {!r})'.format(
                self.__class__.__name__,
                self.id,
                self.system_admin,
                self.name,
                self.email,
                self.email_verification_sent_at,
                self.email_verified_at,
                self.is_api_key,
                self.acknowledgments,
                self.created_at,
                self.updated_at,
                self.deleted_at,
                self.brand,
                self.gravatar,
                self.team_admin,
                self.team_enabled,
                self.team_role,
                self.merchant_options,
                self.is_default
            )

        return repr
