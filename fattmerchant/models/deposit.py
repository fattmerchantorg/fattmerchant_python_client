from datetime import datetime


class DepositBatch(object):
    """
    Deposit batch model class
    """
    def __init__(self, data):
        self.batch_id = data.get("batch_id")
        """ Id of the deposit batch """

        self.batched_at = datetime.strptime(
            data.get("batched_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("batched_at") else None
        """ When the deposit batch was created """

        self.last_transaction = data.get("last_transaction")
        """ The last transaction of the deposit batch """

        self.count = data.get("count")
        """ The number of deposits in the batch """

        self.sum = data.get("sum")
        """ The sum of the totals from the deposits in the batch """

        self.avg = data.get("avg")
        """ The avg of the totals from the deposits in the batch """

        self.min = data.get("min")
        """ The minimum total of the totals from the deposits in the batch """

        self.max = data.get("max")
        """ The maximum total of the totals from the deposits in the batch """

        self.std = data.get("std")
        """
        The standard deviation of the totals from the deposits in the batch
        """

        self.fees = data.get("fees")
        """
        The total amount of money the merchant is paying in fees for all
        deposits
        """
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


class DepositDetails(object):
    """
    Deposit details model class
    """
    def __init__(self, data):
        self.batch_id = data.get("batch_id", None)
        """ Id of the deposit batch """

        self.batched_at = datetime.strptime(
            data.get("batched_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("batched_at") else None
        """ When the deposit batch was created """

        self.auth_id = data.get("auth_id", None)
        """ The auth id of the deposit """

        self.created_at = datetime.strptime(
            data.get("created_at"), '%Y-%m-%d %H:%M:%S'
        ) if data.get("created_at") else None
        """ When the deposit was created """

        self.total = data.get("total", None)
        """ The total amount of the deposit """

        self.last_four = data.get("last_four", None)
        """
        The last four numbers of the credit card used for the deposit
        """

        self.card_type = data.get("card_type", None)
        """ The type of credit card used for the deposit """
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
