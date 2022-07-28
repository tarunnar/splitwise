from rest_framework import exceptions

from app import constants
from app.models import GroupBalances


class GroupBalancesRepository(object):

    @classmethod
    def get_group_balances_by_filter(cls, filters):
        return GroupBalances.objects.filter(**filters)

    @classmethod
    def create_group_balances(cls, objs):
        return GroupBalances.objects.bulk_create(
            objs
        )

    @classmethod
    def get_group_balances(cls, objs):
        return GroupBalances.objects.bulk_create(objs)

    @classmethod
    def update_group_balances(cls, objs, fields):
        return GroupBalances.objects.bulk_update(objs, fields)

