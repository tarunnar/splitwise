from rest_framework import exceptions
from app.repositeries.bill import BillRepository
from app.repositeries.group_balances import GroupBalancesRepository
from app import constants
from app.models import *
from django.db import transaction


class BillService(object):

    @classmethod
    def add_bill(cls, group_id, paid_by, total_amount, split_type, split_distribution):
        percentage_sum = 0
        if split_type.upper() == Bill.SplitType.PERCENTAGE.name:
            for record in split_distribution:
                percentage_sum += int(record["amount"])
                record["amount"] = float(record["amount"]) * float(total_amount) * 0.01

            if percentage_sum != 100:
                raise exceptions.APIException({
                    constants.MESSAGE_KEY_STR: f"please put complete percentage bill split"
                })
        split_type = vars(Bill.SplitType)["_member_map_"][split_type.upper()]

        group_balance_qs = GroupBalancesRepository.get_group_balances_by_filter({
            "group_id": group_id
        })
        group_balances = []
        with transaction.atomic():
            BillRepository.add_bill(
                group_id,
                paid_by,
                total_amount,
                split_type,
                split_distribution
            )
            if not group_balance_qs:
                for record in split_distribution:
                    if paid_by != record.get("user_id"):
                        group_balances.extend(
                            [
                                GroupBalances(
                                    group_id=group_id,
                                    user_to_receive_id=paid_by,
                                    user_to_pay_id=record.get("user_id"),
                                    amount=record["amount"]
                                ),
                                GroupBalances(
                                    group_id=group_id,
                                    user_to_receive_id=record.get("user_id"),
                                    user_to_pay_id=paid_by,
                                    amount=-record["amount"]
                                )
                            ]
                        )
                GroupBalancesRepository.create_group_balances(group_balances)
            else:
                group_balances_map = {}
                for gb in group_balance_qs:
                    group_balances_map[(gb.user_to_receive_id, gb.user_to_pay_id)] = gb

                for record in split_distribution:
                    if paid_by != record.get("user_id"):
                        key = (paid_by, record.get("user_id"))
                        rev_key = (key[1], key[0])
                        if key in group_balances_map:
                            gb1 = group_balances_map[key]
                            gb2 = group_balances_map[rev_key]
                            amount = record.get("amount")
                            gb1.amount += amount
                            gb2.amount -= amount
                        else:
                            group_balances.extend(
                                [
                                    GroupBalances(
                                        group_id=group_id,
                                        user_to_receive_id=paid_by,
                                        user_to_pay_id=record.get("user_id"),
                                        amount=record["amount"]
                                    ),
                                    GroupBalances(
                                        group_id=group_id,
                                        user_to_receive_id=record.get("user_id"),
                                        user_to_pay_id=paid_by,
                                        amount=-record["amount"]
                                    )
                                ]
                            )
                GroupBalancesRepository.create_group_balances(group_balances)
                GroupBalancesRepository.update_group_balances(group_balances_map.values(), fields=["amount"])
        return {
            "status": constants.SUCCESS_STATUS,
            "message": "bill added successfully"
        }

    @classmethod
    def get_group_bills(cls, group_id):
        bill_qs = BillRepository.get_bill_by_filter({
            "group_id": group_id
        })
        bills = []
        total_amount = 0
        for record in bill_qs:
            bills.append({
                "id": record.id,
                "group_id": record.group_id,
                "user_paid": record.paid_by_id,
                "total_amount": record.total_amount,
                "split_type": record.split_type,
                "split_distribution": record.expense_splits
            })
            total_amount += record.total_amount
        return {
            "status": constants.SUCCESS_STATUS,
            "data": {
                "bills": bills,
                "total_bills_amount": total_amount
            }
        }
