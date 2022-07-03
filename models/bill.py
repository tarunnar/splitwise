class Bill(object):
    def __init__(self):
        self._id = None
        self._paid_by = None
        self._group_id = None
        self._split_perc = None
        self._amount = None

    def get_id(self):
        return self._id

    def set_id(self, _id):
        self._id = _id

    def set_group_id(self, _group_id):
        self._group_id = _group_id

    def get_group_id(self):
        return self._group_id

    def get_paid_by(self):
        return self._paid_by

    def set_paid_by(self, paid_by):
        self._paid_by = paid_by

    def set_split_perc(self, split_perc):
        self._split_perc = split_perc

    def get_split_perc(self):
        return self._split_perc

    def get_amount(self):
        return self._amount

    def set_amount(self, _amount):
        self._amount = _amount
