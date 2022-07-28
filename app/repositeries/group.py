from rest_framework import exceptions

from app import constants
from app.models import Group


class GroupRepository(object):
    @classmethod
    def get_group_by_id(cls, id):
        try:
            return Group.objects.get(id=id)
        except Exception as e:
            raise exceptions.APIException({
                constants.MESSAGE_KEY_STR: f"group with id:{id} not exists"
            })

    @classmethod
    def get_group_by_filter(cls, filters):
        return Group.objects.filter(**filters)

    @classmethod
    def create_group(cls, name, description, owner):
        return Group.objects.create(
            name=name,
            description=description,
            owner=owner
        )