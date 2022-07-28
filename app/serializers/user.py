from rest_framework import serializers
from rest_framework import exceptions
from app import constants


class UserSerializer(serializers.BaseSerializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def to_internal_value(self, data):
        email = data.get("email")

        if not email:
            raise exceptions.ValidationError(
                {
                    constants.MESSAGE_KEY_STR: constants.EMAIL_MISSING
                }
            )
        password = data.get("password")

        if not password:
            raise exceptions.ValidationError(
                {
                    constants.MESSAGE_KEY_STR: constants.PASSWORD_MISSING
                }
            )
        name = data.get("name")

        if not name:
            raise exceptions.ValidationError(
                {
                    constants.MESSAGE_KEY_STR: constants.NAME_MISSING
                }
            )
        return data

    def to_representation(self, instance):
        return instance

