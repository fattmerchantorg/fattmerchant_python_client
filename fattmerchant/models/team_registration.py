from datetime import datetime


class TeamRegistration(object):
    """
    Team registration model class
    """
    def __init__(self, data):
        self.email = data.get("email")
        """ Email for this registration """

        self.first_name = data.get("first_name")
        """ First name for this registration """

        self.last_name = data.get("last_name")
        """ Last name for this registration """

        self.is_flat_rate = data.get("is_flat_rate")
        """ whether this is a flat rate plan """

        self.plan_txamnt = data.get("plan_txamnt")
        """ dollar amount per transaction eg. 0.08"""

        self.refund_policy = data.get("refund_policy")
        """ merchant business refund """

        self.business_fax = data.get("business_fax")
        """ merchant fax number only digits """

        self.business_legal_name = data.get("business_legal_name")
        """ merchant business legal """ 
        
        self.business_dba = data.get("business_dba")
        """ merchant business dba """

        self.business_website = data.get("business_website")
        """ merchant business website address (including http://) """ 

        self.business_phone_number = data.get("business_phone_number")
        """ merchant business phone number """

        self.business_address_1 = data.get("business_address_1") 
        """ merchant business address line 1 """ 

        self.business_address_2 = data.get("business_address_2")
        """ merchant business address line 2 """

        self.business_address_city = data.get("business_address_city")
        """ merchant business city """

        self.business_address_state = data.get("business_address_state")
        """ merchant business state (two letter) """
        
        self.business_address_zip = data.get("business_address_zip") 
        """ merchant business zip """

        self.business_address_country = data.get("business_address_country");
        """ merchant business state iso-3 """ 

        self.business_location_address_1 = data.get("business_location_address_1")
        """ merchant business address line 1 """

        self.business_location_address_2 = data.get("business_location_address_2")
        """ merchant business address line 2 """ 

        self.business_location_address_city = data.get("business_location_address_city")
        """ merchant business city """

        self.business_location_address_state = data.get("business_location_address_state")
        """ merchant business state two letters """
        
        self.business_location_address_zip = data.get("business_location_address_zip")
        """ merchant business zip """ 

        self.business_location_address_country = data.get("business_location_address_country")
        """ merchant business country iso-3 """

        self.business_location_phone_number = data.get("business_location_phone_number")
        """ merchant business phone number """ 

        self.business_open_date = datetime.strptime(
            data.get("business_open_date"), '%Y-%m-%d'
        ) if data.get("business_open_date") else None
        """ merchant business open date format MM/DD/YYYY """ 

        self.company_type = data.get("company_type")
        """ Company type description """ 

        self.business_tax_id = data.get("business_tax_id")
        """ merchant business taxid format: 99-9999999 """ 

        self.annual_volume = data.get("annual_volume")
        """ merchant volume annual annual_volume """

        self.avg_trans_size = data.get("avg_trans_size")
        """ merchant volume avg """ 

        self.highest_trans_amount = data.get("highest_trans_amount")
        """ merchant volume highest tx highest_trans_amount """ 

        self.card_present_percent = data.get("card_present_percent")
        """ merchant volume card present percent eg: 50 """ 

        self.card_swiped_percent = data.get("card_swiped_percent")
        """ merchant volume card swiped percent eg 50 """ 

        self.card_not_present_percent = data.get("card_not_present_percent")
        """ merchant volume not present eg 15 """ 

        self.moto_percent = data.get("moto_percent")
        """ merchant volume moto percent """

        self.internet = data.get("internet")
        """ merchant volume internet percent """

        self.b2b_percent = data.get("b2b_percent")
        """ merchant volume B2B percent """

        self.international = data.get("international")
        """ merchant volume international percent """ 

        self.bank_routing_number = data.get("bank_routing_number")
        """ billing bank routing number """

        self.bank_account_number = data.get("bank_account_number")
        """ billing bank account number """ 

        self.chosen_plan = data.get("chosen_plan")
        """ merchant Plan Choice """ 

        self.chosen_processing_method = data.get("chosen_processing_method")
        """ ProcessingMethod chosen_processing_method """ 

        self.reason_for_applying = data.get("reason_for_applying")
        """ merchant business aplication reason eg. "Processor Change" """

        self.service_you_provide = data.get("service_you_provide")
        """ merchant business what is sold description """ 

        self.plan_nabu = data.get("plan_nabu")
        """ NABU eg. 0.06 """ 

        self.bus_type = data.get("bus_type")
        """ merchant btype """ 

        self.principal_owners_name = data.get("principal_owners_name")
        """ merchant owner principal name """ 

        self.job_title = data.get("job_title")
        """ merchant owner title """ 

        self.user_dob = datetime.strptime(
            data.get("user_dob"), '%Y-%m-%d'
        ) if data.get("user_dob") else None
        """ Owner dob date format MM/DD/YYYY """ 

        self.phone_number = data.get("phone_number")
        """ owner/signer phone number """

        self.owner_address_1 = data.get("owner_address_1")
        """ owner/signer Address line 1 """ 

        self.owner_address_2 = data.get("owner_address_2")
        """ owner/signer Address line 2 """

        self.owner_address_city = data.get("owner_address_city")
        """ owner/signer City """ 

        self.owner_address_state = data.get("owner_address_state")
        """ owner/signer State """ 

        self.owner_address_country = data.get("owner_address_country")
        """owner/signer country """ 

        self.owner_address_zip = data.get("owner_address_zip")
        """ owner/signer Zip """ 

        self.user_ssn = data.get("user_ssn")
        """ owner/signer social security number """

        self.created_at = datetime.strptime(
            data.get("created_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("created_at") else None
        """ When the registration was created """

        self.updated_at = datetime.strptime(
            data.get("updated_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("updated_at") else None
        """ When the registration was updated """

        self.deleted_at = datetime.strptime(
            data.get("deleted_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("deleted_at") else None
        """ When the registration was deleted """
    def __repr__(self):
        repr = '{}(' \
            'email: {!r}, ' \
            'first_name: {!r}, ' \
            'last_name: {!r}, ' \
            'is_flat_rate: {!r}, ' \
            'plan_txamnt: {!r}, ' \
            'refund_policy: {!r}, ' \
            'business_fax: {!r}, ' \
            'business_legal_name: {!r}, ' \
            'business_dba: {!r}, ' \
            'business_website: {!r}, ' \
            'business_phone_number: {!r}, ' \
            'business_address_1: {!r}, ' \
            'business_address_2: {!r}, ' \
            'business_address_city: {!r}, ' \
            'business_address_state: {!r}, ' \
            'business_address_zip: {!r}, ' \
            'business_address_country: {!r}, ' \
            'business_location_address_1: {!r}, ' \
            'business_location_address_2: {!r}, ' \
            'business_location_address_city: {!r}, ' \
            'business_location_address_state: {!r}, ' \
            'business_location_address_country: {!r}, ' \
            'business_location_phone_number: {!r}, ' \
            'business_open_date: {!r}, ' \
            'company_type: {!r}, ' \
            'business_tax_id: {!r}, ' \
            'annual_volume: {!r}, ' \
            'avg_trans_size: {!r}, ' \
            'highest_trans_amount: {!r}, ' \
            'card_present_percent: {!r}, ' \
            'card_swiped_percent: {!r}, ' \
            'card_not_present_percent: {!r}, ' \
            'card_swiped_percent: {!r}, ' \
            'card_not_present_percent: {!r}, ' \
            'moto_percent: {!r}, ' \
            'internet: {!r}, ' \
            'b2b_percent: {!r}, ' \
            'international: {!r}, ' \
            'bank_routing_number: {!r}, ' \
            'chosen_plan: {!r}, ' \
            'chosen_processing_method: {!r}, ' \
            'reason_for_applying: {!r}, ' \
            'service_you_provide: {!r}, ' \
            'plan_nabu: {!r}, ' \
            'bus_type: {!r}, ' \
            'principal_owners_name: {!r}, ' \
            'job_title: {!r}, ' \
            'user_dob: {!r}, ' \
            'phone_number: {!r}, ' \
            'owner_address_1: {!r}, ' \
            'owner_address_2: {!r}, ' \
            'owner_address_city: {!r}, ' \
            'owner_address_state: {!r}, ' \
            'owner_address_country: {!r}, ' \
            'owner_address_zip: {!r}, ' \
            'user_ssn: {!r}, ' \
            'created_at: {!r}, ' \
            'updated_at: {!r}, ' \
            'deleted_at: {!r})'.format(
                self.__class__.__name__,
                self.email,
                self.first_name,
                self.last_name,
                self.is_flat_rate,
                self.plan_txamnt,
                self.refund_policy,
                self.business_fax,
                self.business_legal_name,
                self.business_dba,
                self.business_website,
                self.business_phone_number,
                self.business_address_1,
                self.business_address_2,
                self.business_address_city,
                self.business_address_state,
                self.business_address_zip,
                self.business_address_country,
                self.business_location_address_1,
                self.business_location_address_2,
                self.business_location_address_city,
                self.business_location_address_state,
                self.business_location_address_country,
                self.business_location_phone_number,
                self.business_open_date,
                self.company_type,
                self.business_tax_id,
                self.annual_volume,
                self.avg_trans_size,
                self.highest_trans_amount,
                self.card_present_percent,
                self.card_swiped_percent,
                self.card_not_present_percent,
                self.card_swiped_percent,
                self.card_not_present_percent,
                self.moto_percent,
                self.internet,
                self.b2b_percent,
                self.international,
                self.bank_routing_number,
                self.chosen_plan,
                self.chosen_processing_method,
                self.reason_for_applying,
                self.service_you_provide,
                self.plan_nabu,
                self.bus_type,
                self.principal_owners_name,
                self.job_title,
                self.user_dob,
                self.phone_number,
                self.owner_address_1,
                self.owner_address_2,
                self.owner_address_city,
                self.owner_address_state,
                self.owner_address_country,
                self.owner_address_zip,
                self.user_ssn,
                self.created_at,
                self.updated_at,
                self.deleted_at
            )

        return repr
