from datetime import datetime


class User():
    """
    User model class
    """
    def __init__(self, data):
        self.id = data.get("id")
        self.system_admin = data.get("system_admin")
        self.name = data.get("name")
        self.email = data.get("email")
        self.email_verification_sent_at = datetime.strptime(
            data.get("email_verification_sent_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("email_verification_sent_at") else None
        self.email_verified_at = data.get("email_verified_at")
        self.is_api_key = data.get("is_api_key")
        self.acknowledgments = data.get("acknowledgments")
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
        self.gravatar = data.get("gravatar")
        self.team_admin = data.get("team_admin")
        self.team_enabled = data.get("team_enabled")
        self.team_role = data.get("team_role")
        self.merchant_options = data.get("merchant_options")
        self.is_default = data.get("is_default")

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
