from datetime import datetime

from fattmerchant.models import Customer, Merchant, PaymentMethod, User


class Transaction():
    """
    Transaction model class
    """
    def __init__(self, data):
        self.id = data.get("id")
        self.invoice_id = data.get("invoice_id")
        self.reference_id = data.get("reference_id")
        self.recurring_transaction_id = data.get("recurring_transaction_id")
        self.auth_id = data.get("auth_id")
        self.type = data.get("type")
        self.source = data.get("source")
        self.is_merchant_present = data.get("is_merchant_present")
        self.merchant_id = data.get("merchant_id")
        self.user_id = data.get("user_id")
        self.customer_id = data.get("customer_id")
        self.payment_method_id = data.get("payment_method_id")
        self.is_manual = data.get("is_manual")
        self.success = data.get("success")
        self.message = data.get("message")
        self.meta = data.get("meta")
        self.total = data.get("total")
        self.method = data.get("method")
        self.pre_auth = data.get("pre_auth")
        self.is_captured = data.get("is_captured")
        self.last_four = data.get("last_four")
        self.interchange_code = data.get("interchange_code")
        self.interchange_fee = data.get("interchange_fee")
        self.batch_id = data.get("batch_id")
        self.batched_at = datetime.strptime(
            data.get("batched_at"),
            '%Y-%m-%d %H:%M:%S') if data.get("batched_at") else None
        self.emv_response = data.get("emv_response")
        self.avs_response = data.get("avs_response")
        self.cvv_response = data.get("cvv_response")
        self.pos_entry = data.get("pos_entry")
        self.pos_salesperson = data.get("pos_salesperson")
        self.receipt_email_at = data.get("receipt_email_at")
        self.receipt_sms_at = data.get("receipt_sms_at")
        self.settled_at = datetime.strptime(
            data.get("settled_at"),
            '%Y-%m-%d %H:%M:%S') if data.get("settled_at") else None
        self.created_at = datetime.strptime(
            data.get("created_at"),
            '%Y-%m-%d %H:%M:%S') if data.get("created_at") else None
        self.updated_at = datetime.strptime(
            data.get("updated_at"),
            '%Y-%m-%d %H:%M:%S') if data.get("updated_at") else None
        self.source_ip = data.get("source_ip")
        self.gateway_id = data.get("gateway_id")
        self.issuer_auth_code = data.get("issuer_auth_code")
        self.total_refunded = data.get("total_refunded")
        self.is_refundable = data.get("is_refundable")
        self.is_voided = data.get("is_voided")
        self.is_voidable = data.get("is_voidable")
        self.schedule_id = data.get("schedule_id")
        self.child_captures = data.get("child_captures"),
        self.parent_auth = data.get("parent_auth"),
        self.gateway_name = data.get("gateway_name"),
        self.response = data.get("response")
        self.is_settling = data.get("is_settling")
        self.customer = Customer(data.get("customer")) \
            if data.get("customer") else None

        child_transactions = data.get("child_transactions")
        if child_transactions:
            self.child_transactions = []

            for transaction in child_transactions:
                self.child_transactions.append(Transaction(transaction))
        else:
            self.child_transactions = None

        self.files = data.get("files")
        self.payment_method = PaymentMethod(data.get("payment_method")) \
            if data.get("payment_method") else None
        self.user = User(data.get("user")) \
            if data.get("user") else None
        self.merchant = Merchant(data.get("merchant")) \
            if data.get("merchant") else None

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
