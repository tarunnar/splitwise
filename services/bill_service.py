from models.bill import Bill
from services.bill_service_interface import BillServiceInterface
from collections import defaultdict


def default_factory():
    return 0


class BillService(BillServiceInterface):
    bills = dict()

    def get_group_balance(self, group_id):
        user_balances = defaultdict(default_factory)
        for bill_id in self.__class__.bills:
            bill = self.__class__.bills[bill_id]

            if bill.get_group_id() == group_id:
                bill_amount = bill.get_amount()
                user_balances[bill.get_paid_by()] += bill_amount
                split_perc = bill.get_split_perc()
                for user in split_perc:
                    user_balances[user] -= (split_perc[user] * bill_amount) * .01

        return user_balances

    def add_bill(self, _id, _paid_by, _group_id, _split_perc, _amount):
        bill = Bill()
        bill.set_id(_id)
        bill.set_group_id(_group_id)
        bill.set_paid_by(_paid_by)
        bill.set_split_perc(_split_perc)
        bill.set_amount(_amount)
        self.__class__.bills[_id] = bill
        return bill
