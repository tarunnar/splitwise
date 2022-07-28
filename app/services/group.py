from rest_framework import exceptions

from app import constants
from app.repositeries.group import GroupRepository
from app.repositeries.group_members import GroupMembersRepository
from django.db import transaction

import logging

logger = logging.getLogger(__name__)


class GroupService(object):

    @classmethod
    def create_group(cls, owner, name, description):
        group_qs = GroupRepository.get_group_by_filter({"name": name})
        if group_qs:
            raise exceptions.APIException({
                constants.MESSAGE_KEY_STR: f"group with name:{name} already exists"
            })
        with transaction.atomic():
            group = GroupRepository.create_group(
                name,
                description,
                owner
            )
            GroupMembersRepository.create_group_member(
                group_id=group.id,
                user_id=owner.id
            )
        return {
            "status": constants.SUCCESS_STATUS,
            "group": {
                "id": group.id,
                "name": group.name,
                "owner_user_id": group.owner.id,
                "owner_email": group.owner.email,
                "description": group.description
            }
        }
