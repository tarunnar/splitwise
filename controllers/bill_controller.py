class BillController:
    def __init__(self, bill_service_interface):
        self.bill_service_interface = bill_service_interface

    def add_bill(self, _id, _paid_by, _group_id, _split_perc, _amount):
        return self.bill_service_interface.add_bill(_id, _paid_by, _group_id, _split_perc, _amount)

    def get_group_balance(self, _group_id):
        return self.bill_service_interface.get_group_balance(_group_id)
