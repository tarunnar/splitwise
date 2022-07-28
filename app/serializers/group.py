from rest_framework import serializers
from rest_framework import exceptions
from app import constants
from app.models import *


class GroupSerializer(serializers.BaseSerializer):
    payment_modes_dict = dict(Bill.SplitType.choices)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def to_internal_value(self, data):
        name = data.get("name")
        if not name:
            raise exceptions.ValidationError(
                {
                    constants.MESSAGE_KEY_STR: constants.NAME_MISSING
                }
            )
        description = data.get("description")
        if not description:
            raise exceptions.ValidationError(
                {
                    constants.MESSAGE_KEY_STR: constants.GROUP_DESCRIPTION_MISSING
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
