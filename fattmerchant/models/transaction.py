from datetime import datetime

from fattmerchant.models import Customer, Merchant, PaymentMethod, User


class Transaction(object):
    """
    Transaction model class
    """
    def __init__(self, data):
        self.id = data.get("id")
        """ Id of the transaction """

        self.invoice_id = data.get("invoice_id")
        """ Invoice id of the transaction """

        self.reference_id = data.get("reference_id")
        """ Reference id of the transaction """

        self.recurring_transaction_id = data.get("recurring_transaction_id")
        """ Recurring transaction id of the transaction """

        self.auth_id = data.get("auth_id")
        """ Auth id of the transaction """

        self.type = data.get("type")
        """ The transaction type """

        self.source = data.get("source")
        """
        Optional field to track the source of a transaction made
        outside of Omni
        """

        self.is_merchant_present = data.get("is_merchant_present")
        """
        Whether the merchant was present when the transaction was created
        """

        self.merchant_id = data.get("merchant_id")
        """ Merchant id of the transaction """

        self.user_id = data.get("user_id")
        """ User id of the transaction """

        self.customer_id = data.get("customer_id")
        """ Customer id of the transaction """

        self.payment_method_id = data.get("payment_method_id")
        """ Payment method id of the transaction """

        self.is_manual = data.get("is_manual")
        """ Whether the transaction was created manually or not """

        self.success = data.get("success")
        """ Whether the transaction was successful or not """

        self.message = data.get("message")
        """ Error message of an unsuccesful transaction """

        self.meta = data.get("meta")
        """ Any meta data of the transaction """

        self.total = data.get("total")
        """ Total of the transaction """

        self.method = data.get("method")
        """ The payment method type for the transaction """

        self.pre_auth = data.get("pre_auth")
        """ Whether the transaction is a pre authorization transaction """

        self.is_captured = data.get("is_captured")
        """ Whether the pre auth transaction is captured or not """

        self.last_four = data.get("last_four")
        """ Last for numbers of the payment method for the transaction """

        self.interchange_code = data.get("interchange_code")
        """ Interchange classification """

        self.interchange_fee = data.get("interchange_fee")
        """ Fees associated with transaction """

        self.batch_id = data.get("batch_id")
        """ (Not used) """

        self.batched_at = datetime.strptime(
            data.get("batched_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("batched_at") else None
        """ When the transaction was batched """

        self.emv_response = data.get("emv_response")
        """ Response from card present emv transactions """

        self.avs_response = data.get("avs_response")
        """ Response from address verification system """

        self.cvv_response = data.get("cvv_response")
        """ Response from card verification """

        self.pos_entry = data.get("pos_entry")
        """ Additional details from point of sale system """

        self.pos_salesperson = data.get("pos_salesperson")
        """ Additional details from point of sale system """

        self.receipt_email_at = data.get("receipt_email_at")
        """ When the reciept email was sent """

        self.receipt_sms_at = data.get("receipt_sms_at")
        """ When the reciept text was sent """

        self.settled_at = datetime.strptime(
            data.get("settled_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("settled_at") else None
        """ When the transaction was settled """

        self.created_at = datetime.strptime(
            data.get("created_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("created_at") else None
        """ When the transaction was created """

        self.updated_at = datetime.strptime(
            data.get("updated_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("updated_at") else None
        """ When the transaction was updated """

        self.source_ip = data.get("source_ip")
        """ Where the transaction was made """

        self.gateway_id = data.get("gateway_id")
        """ Gateway id of the transaction """

        self.issuer_auth_code = data.get("issuer_auth_code")
        """ Authorization code from the gateway for the transaction """

        self.total_refunded = data.get("total_refunded")
        """ Total amount that was refunded of the transaction """

        self.is_refundable = data.get("is_refundable")
        """ Whether the transaction is refundable or not """

        self.is_voided = data.get("is_voided")
        """ Whether the transaction was voided or not """

        self.is_voidable = data.get("is_voidable")
        """ Whether the transaction is voidable or not """

        self.schedule_id = data.get("schedule_id")
        """ Id of the associated schedule for this transaction  """

        self.child_captures = data.get("child_captures")
        """ Any child transaction captures if the transaction is a pre auth """

        self.parent_auth = data.get("parent_auth")
        """ The parent transaction if this transaction is a capture """

        self.gateway_name = data.get("gateway_name")
        """ Gateway name for the transaction """

        self.response = data.get("response")
        """ Optional JSON field to store the gateway response """

        self.is_settling = data.get("is_settling")
        """ Whether the transaction is settling or not """

        self.customer = Customer(data.get("customer")) \
            if data.get("customer") else None
        """ The customer for the transaction """

        child_transactions = data.get("child_transactions")
        if child_transactions:
            self.child_transactions = []

            for transaction in child_transactions:
                self.child_transactions.append(Transaction(transaction))
        else:
            self.child_transactions = None
        """ Any child transactions that are linked to the transaction """

        self.files = data.get("files")
        """ Any files that are linked to the transaction """

        self.payment_method = PaymentMethod(data.get("payment_method")) \
            if data.get("payment_method") else None
        """ Payment method for the transaction """

        self.user = User(data.get("user")) \
            if data.get("user") else None
        """ User for the transaction """

        self.merchant = Merchant(data.get("merchant")) \
            if data.get("merchant") else None
        """ Merchant for the transaction """

    def __repr__(self):
        repr = '{}(' \
            'id: {!r}, ' \
            'invoice_id: {!r}, ' \
            'reference_id: {!r}, ' \
            'recurring_transaction_id: {!r}, ' \
            'auth_id: {!r}, ' \
            'type: {!r}, ' \
            'source: {!r}, ' \
            'is_merchant_present: {!r}, ' \
            'merchant_id: {!r}, ' \
            'user_id: {!r}, ' \
            'customer_id: {!r}, ' \
            'payment_method_id: {!r}, ' \
            'is_manual: {!r}, ' \
            'success: {!r}, ' \
            'message: {!r}, ' \
            'meta: {!r}, ' \
            'total: {!r}, ' \
            'method: {!r}, ' \
            'pre_auth: {!r}, ' \
            'is_captured: {!r}, ' \
            'last_four: {!r}, ' \
            'interchange_code: {!r}, ' \
            'interchange_fee: {!r}, ' \
            'batch_id: {!r}, ' \
            'batched_at: {!r}, ' \
            'emv_response: {!r}, ' \
            'avs_response: {!r}, ' \
            'cvv_response: {!r}, ' \
            'pos_entry: {!r}, ' \
            'pos_salesperson: {!r}, ' \
            'receipt_email_at: {!r}, ' \
            'receipt_sms_at: {!r}, ' \
            'settled_at: {!r}, ' \
            'created_at: {!r}, ' \
            'updated_at: {!r}, ' \
            'source_ip: {!r}, ' \
            'gateway_id: {!r}, ' \
            'issuer_auth_code: {!r}, ' \
            'total_refunded: {!r}, ' \
            'is_refundable: {!r}, ' \
            'is_voided: {!r}, ' \
            'is_voidable: {!r}, ' \
            'schedule_id: {!r}, ' \
            'child_captures: {!r}, ' \
            'parent_auth: {!r}, ' \
            'gateway_name: {!r}, ' \
            'response: {!r}, ' \
            'is_settling: {!r}, ' \
            'customer: {!r}, ' \
            'child_transactions: {!r}, ' \
            'files: {!r}, ' \
            'payment_method: {!r}, ' \
            'user: {!r}, ' \
            'merchant: {!r})'.format(
                self.__class__.__name__,
                self.id,
                self.invoice_id,
                self.reference_id,
                self.recurring_transaction_id,
                self.auth_id,
                self.type,
                self.source,
                self.is_merchant_present,
                self.merchant_id,
                self.user_id,
                self.customer_id,
                self.payment_method_id,
                self.is_manual,
                self.success,
                self.message,
                self.meta,
                self.total,
                self.method,
                self.pre_auth,
                self.is_captured,
                self.last_four,
                self.interchange_code,
                self.interchange_fee,
                self.batch_id,
                self.batched_at,
                self.emv_response,
                self.avs_response,
                self.cvv_response,
                self.pos_entry,
                self.pos_salesperson,
                self.receipt_email_at,
                self.receipt_sms_at,
                self.settled_at,
                self.created_at,
                self.updated_at,
                self.source_ip,
                self.gateway_id,
                self.issuer_auth_code,
                self.total_refunded,
                self.is_refundable,
                self.is_voided,
                self.is_voidable,
                self.schedule_id,
                self.child_captures,
                self.parent_auth,
                self.gateway_name,
                self.response,
                self.is_settling,
                self.customer,
                self.child_transactions,
                self.files,
                self.payment_method,
                self.user,
                self.merchant
            )

        return repr
