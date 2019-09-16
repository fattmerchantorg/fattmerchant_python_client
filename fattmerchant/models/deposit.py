from datetime import datetime


class DepositBatch():
    """
    Deposit batch model class
    """
    def __init__(self, data):
        self.batch_id = data.get("batch_id")
        self.batched_at = datetime.strptime(
            data.get("batched_at"),
            '%Y-%m-%d %H:%M:%S') if data.get("batched_at") else None
        self.last_transaction = data.get("last_transaction")
        self.count = data.get("count")
        self.sum = data.get("sum")
        self.avg = data.get("avg")
        self.min = data.get("min")
        self.max = data.get("max")
        self.std = data.get("std")
        self.fees = data.get("fees")

    def __repr__(self):
        repr = '{}(' \
            'batch_id: {!r}, ' \
            'batched_at: {!r}, ' \
            'last_transaction: {!r}, ' \
            'count: {!r}, ' \
            'sum: {!r}, ' \
            'avg:{!r}, '\
            'min: {!r}, ' \
            'max: {!r}, ' \
            'std: {!r}, ' \
            'fees: {!r})'.format(
                self.__class__.__name__,
                self.batch_id,
                self.batched_at,
                self.last_transaction,
                self.count,
                self.sum,
                self.avg,
                self.min,
                self.max,
                self.std,
                self.fees
            )

        return repr


class DepositBatchDetail():
    """
    Deposit batch detail model class
    """
    def __init__(self, data):
        self.batch_id = data.get("batch_id", None)
        self.batched_at = datetime.strptime(
            data.get("batched_at"),
            '%Y-%m-%d %H:%M:%S') if data.get("batched_at") else None
        self.auth_id = data.get("auth_id", None)
        self.created_at = datetime.strptime(
            data.get("created_at"),
            '%Y-%m-%d %H:%M:%S') if data.get("created_at") else None
        self.total = data.get("total", None)
        self.fees = data.get("fees", None)
        self.last_four = data.get("last_four", None)
        self.card_type = data.get("card_type", None)

    def __repr__(self):
        repr = '{}(' \
            'batch_id: {!r}, ' \
            'batched_at: {!r}, ' \
            'auth_id: {!r}, ' \
            'created_at: {!r}, ' \
            'total: {!r}, ' \
            'fees:{!r}, '\
            'last_four: {!r}, ' \
            'card_type: {!r})'.format(
                self.__class__.__name__,
                self.batched_at,
                self.batch_id,
                self.auth_id,
                self.created_at,
                self.total,
                self.fees,
                self.last_four,
                self.card_type,
            )

        return repr
