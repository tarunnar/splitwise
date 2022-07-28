from app.models import *

from rest_framework import serializers
from rest_framework import exceptions
from app import constants
from app.models import *


class BillSerializer(serializers.BaseSerializer):
    bill_split_choices = dict(Bill.SplitType.choices)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def to_internal_value(self, data):
        group_id = data.get("group_id")
        if not group_id:
            raise exceptions.ValidationError(
                {
                    constants.MESSAGE_KEY_STR: constants.GROUP_ID_MISSING
                }
            )
        paid_by_id = data.get("paid_by")
        if not paid_by_id:
            raise exceptions.ValidationError(
                {
                    constants.MESSAGE_KEY_STR: constants.GROUP_DESCRIPTION_MISSING
                }
            )

        total_amount = data.get("total_amount")
        if not total_amount:
            raise exceptions.ValidationError(
                {
                    constants.MESSAGE_KEY_STR: constants.TOTAL_AMOUNT_MISSING
                }
            )

        split_type = data.get("split_type")
        if not split_type:
            raise exceptions.ValidationError(
                {
                    constants.MESSAGE_KEY_STR: constants.SPLIT_TYPE_MISSING
                }
            )
        if split_type.upper() not in BillSerializer.bill_split_choices.values():
            raise exceptions.ValidationError(
                {
                    constants.MESSAGE_KEY_STR: constants.SPLIT_TYPE_MISSING
                }
            )

        expense_splits = data.get("expense_splits")
        if not expense_splits:
            raise exceptions.ValidationError(
                {
                    constants.MESSAGE_KEY_STR: constants.EXPENSE_SPLIT_MISSING
                }
            )

        return data

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
            "owner_user_id": instance.owner.id,
            "owner_email_id": instance.owner.email,
            "description": instance.description
        }
