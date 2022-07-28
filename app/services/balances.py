from rest_framework import exceptions
from app.repositeries.bill import BillRepository
from app.repositeries.group_balances import GroupBalancesRepository
from app import constants
from app.models import *
from django.db import transaction


class GroupBalanceService(object):

    @classmethod
    def get_group_balances(self, group_id):
        group_balance_qs = GroupBalancesRepository.get_group_balances_by_filter({
            "group_id": group_id
        })
        group_balances_map = {}
        for gb in group_balance_qs:
            group_balances_map[(gb.user_to_receive_id, gb.user_to_pay_id)] = gb.amount
        computed_user_ids = set()
        group_balances_with_description = []
        for key in group_balances_map:
            if key not in computed_user_ids:
                amount = group_balances_map[key]
                if amount > 0:
                    group_balances_with_description.append(
                        {
                            "user_id_receiver": key[0],
                            "user_id_giver": key[1],
                            "amount": amount,
                            "description": f"user_id: {key[1]} should pay {amount} to {key[0]}"
                        }
                    )
                else:
                    group_balances_with_description.append(
                        {
                            "user_id_receiver": key[1],
                            "user_id_giver": key[0],
                            "amount": -amount,
                            "description": f"user_id: {key[0]} should pay {-amount} to {key[1]}"
                        }
                    )
                computed_user_ids.update([(key[0], key[1]), (key[1], key[0])])
        return {
            "status": constants.SUCCESS_STATUS,
            "group_balances": group_balances_with_description
        }

    @classmethod
    def get_user_balances(cls, group_id, user_id):
        group_balance_qs = GroupBalancesRepository.get_group_balances_by_filter({
            "group_id": group_id,
            "user_to_receive_id": user_id
        })
        group_balances_map = {}
        for gb in group_balance_qs:
            group_balances_map[(gb.user_to_receive_id, gb.user_to_pay_id)] = gb.amount

        group_balances_with_description = []
        for key in group_balances_map:
            amount = group_balances_map[key]
            if amount > 0:
                group_balances_with_description.append(
                    {
                        "user_id_receiver": key[0],
                        "user_id_giver": key[1],
                        "amount": amount,
                        "description": f"You should get amount: {amount} from user_id:{key[1]}"
                    }
                )
            else:
                group_balances_with_description.append(
                    {
                        "user_id_receiver": key[1],
                        "user_id_giver": key[0],
                        "amount": -amount,
                        "description": f"you should pay amount: {-amount} to user_id:{key[1]}"
                    }
                )
        return {
            "status": constants.SUCCESS_STATUS,
            "group_balances": group_balances_with_description
        }
