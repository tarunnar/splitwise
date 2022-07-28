from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status, exceptions
from app.serializers.group import GroupSerializer
from app import constants
from app.services.balances import GroupBalanceService
from app.services.group import GroupService
from app.views.mixins.auth_mixin import AuthMixin


class GroupBalancesView(AuthMixin, APIView):
    def get(self, request, *args, **kwargs):
        group_id = request.query_params.get("group_id")
        if not group_id:
            raise exceptions.ValidationError(
                {
                    constants.MESSAGE_KEY_STR: constants.GROUP_ID_MISSING
                }
            )
        group_balances_response = GroupBalanceService.get_group_balances(
            group_id,
        )
        if group_balances_response[constants.STATUS_KEY_STR] == constants.SUCCESS_STATUS:
            return JsonResponse(
                status=status.HTTP_201_CREATED,
                data={
                    constants.MESSAGE_KEY_STR: constants.GROUP_BALANCES_FETCH_SUCCESS,
                    "group_balances": group_balances_response.get("group_balances")
                }
            )
        return JsonResponse(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={
                    constants.MESSAGE_KEY_STR: constants.GROUP_BALANCES_FETCH_FAILURE
                }
            )
