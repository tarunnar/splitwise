from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from app import constants
from app.services.group_members import GroupMembersService
from app.views.mixins.auth_mixin import AuthMixin


class GroupMembersView(AuthMixin, APIView):
    def post(self, request, *args, **kwargs):
        user = kwargs.get("user_id")
        group_id = request.data.get("group_id")
        if not group_id:
            return JsonResponse(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    constants.MESSAGE_KEY_STR: constants.MESSAGE_KEY_STR,
                }
            )
        group_membership_resp = GroupMembersService.register_to_group(group_id, user.id)
        if group_membership_resp[constants.STATUS_KEY_STR] == constants.SUCCESS_STATUS:
            return JsonResponse(
                status=status.HTTP_201_CREATED,
                data={
                    constants.MESSAGE_KEY_STR: "user registered to group successfully",
                }
            )
        return JsonResponse(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={
                    constants.MESSAGE_KEY_STR: constants.GROUP_REGISTRATION_FAILURE
                }
            )

    def get(self, request, *args, **kwargs):
        group_id = request.query_params.get("group_id")
        if not group_id:
            return JsonResponse(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    constants.MESSAGE_KEY_STR: constants.MESSAGE_KEY_STR,
                }
            )
        group_membership_resp = GroupMembersService.get_group_members(group_id)
        if group_membership_resp[constants.STATUS_KEY_STR] == constants.SUCCESS_STATUS:
            return JsonResponse(
                status=status.HTTP_201_CREATED,
                data={
                    "group_members": group_membership_resp["group_members"]
                }
            )
        return JsonResponse(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={
                    constants.MESSAGE_KEY_STR: constants.GROUP_MEMBERSHIP_FETCH_FAILURE
                }
            )