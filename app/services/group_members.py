from rest_framework import exceptions

from app import constants
from app.repositeries.group_members import GroupMembersRepository

import logging

logger = logging.getLogger(__name__)


class GroupMembersService(object):

    @classmethod
    def register_to_group(cls, group_id, user_id):
        group_qs = GroupMembersRepository.get_group_members_by_filter(
            {
                "group_id": group_id,
                "user_id": user_id
             }
        )
        if group_qs:
            raise exceptions.APIException({
                constants.MESSAGE_KEY_STR: f"user already registered in group"
            })
        group_members = GroupMembersRepository.create_group_member(
            group_id=group_id,
            user_id=user_id
        )
        return {
            "status": constants.SUCCESS_STATUS,
            "group": {
                "id": group_members.id,
                "group_id": group_members.group.id,
                "user_id": group_members.user.id,
            }
        }

    @classmethod
    def get_group_members(cls, group_id):
        group_qs = GroupMembersRepository.get_group_members_by_filter(
            {
                "group_id": group_id,
            }
        )
        return {
            "status": constants.SUCCESS_STATUS,
            "group_members": [{"email": gm.user.email, "user_id": gm.user.id} for gm in group_qs]
        }
