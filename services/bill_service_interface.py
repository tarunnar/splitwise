import abc


class BillServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_bill(self, _id, _paid_by, _group_id, _split_perc, _amount):
        pass

    @abc.abstractmethod
    def get_group_balance(self, group_id):
        pass

