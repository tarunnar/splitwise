from app.models import Bill


class BillRepository(object):
    @classmethod
    def add_bill(cls, group_id, paid_by_id, total_amount, split_type, expense_splits):
        return Bill.objects.create(
            group_id=group_id,
            paid_by_id=paid_by_id,
            total_amount=total_amount,
            split_type=split_type,
            expense_splits=expense_splits
        )

    @classmethod
    def get_bill_by_filter(cls, filters):
        return Bill.objects.filter(**filters)
