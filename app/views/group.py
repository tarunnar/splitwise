from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from app.serializers.group import GroupSerializer
from app import constants
from app.services.group import GroupService
from app.views.mixins.auth_mixin import AuthMixin


class GroupView(AuthMixin, APIView):
    def post(self, request, *args, **kwargs):
        owner = kwargs.get("user_id")
        group_serializer = GroupSerializer(data=request.data)
        group_serializer.is_valid(raise_exception=True)
        validated_data = group_serializer.validated_data
        group_response = GroupService.create_group(
            owner,
            validated_data.get("name"),
            validated_data.get("description")
        )
        if group_response[constants.STATUS_KEY_STR] == constants.SUCCESS_STATUS:
            return JsonResponse(
                status=status.HTTP_201_CREATED,
                data={
                    constants.MESSAGE_KEY_STR: constants.GROUP_CREATION_SUCCESS,
                    "group": group_response.get("group")
                }
            )
        elif group_response[constants.STATUS_KEY_STR] == constants.CONFLICT_STATUS:
            return JsonResponse(
                status=status.HTTP_409_CONFLICT,
                data={
                    constants.MESSAGE_KEY_STR: constants.GROUP_CONFLICT,
                }
            )
        return JsonResponse(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={
                    constants.MESSAGE_KEY_STR: constants.GROUP_CREATION_FAILURE
                }
            )
