from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from app.serializers.bill import BillSerializer
from app import constants
from app.services.bill import BillService
from app.views.mixins.auth_mixin import AuthMixin


class BillView(AuthMixin, APIView):
    def post(self, request, *args, **kwargs):
        bill_serializer = BillSerializer(data=request.data)
        bill_serializer.is_valid(raise_exception=True)
        validated_data = bill_serializer.validated_data
        bill_response = BillService.add_bill(
            validated_data.get("group_id"),
            validated_data.get("paid_by"),
            validated_data.get("total_amount"),
            validated_data.get("split_type"),
            validated_data.get("expense_splits"),
        )
        if bill_response[constants.STATUS_KEY_STR] == constants.SUCCESS_STATUS:
            return JsonResponse(
                status=status.HTTP_201_CREATED,
                data={
                    constants.MESSAGE_KEY_STR: constants.BILL_CREATION_SUCCESS,
                }
            )
        return JsonResponse(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={
                    constants.MESSAGE_KEY_STR: constants.BILL_CREATION_FAILURE
                }
            )

    def get(self, request, *args, **kwargs):
        group_id = request.query_params.get("group_id")
        bill_response = BillService.get_group_bills(group_id)
        if bill_response[constants.STATUS_KEY_STR] == constants.SUCCESS_STATUS:
            return JsonResponse(
                status=status.HTTP_200_OK,
                data={
                    constants.MESSAGE_KEY_STR: constants.BILL_FETCH_SUCCESS,
                    "data": bill_response.get("data")
                }
            )
        return JsonResponse(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={
                    constants.MESSAGE_KEY_STR: constants.BILL_FETCH_FAILURE
                }
            )