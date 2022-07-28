from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status

from app.serializers.user import UserSerializer
from app import constants
from app.services.user import UserSrvice


class UserView(APIView):
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        validated_data = user_serializer.validated_data
        user_response = UserSrvice.create_user(
            validated_data.get("email"),
            validated_data.get("password"),
            validated_data.get("name")
        )
        if user_response[constants.STATUS_KEY_STR] == UserSrvice.success_status:
            return JsonResponse(
                status=status.HTTP_201_CREATED,
                data={
                    constants.MESSAGE_KEY_STR: constants.USER_CREATION_SUCCESS,
                    constants.TOKEN_KEY_STR: user_response.get(constants.TOKEN_KEY_STR)
                }
            )
        elif user_response[constants.STATUS_KEY_STR] == UserSrvice.conflict_status:
            return JsonResponse(
                status=status.HTTP_409_CONFLICT,
                data={
                    constants.MESSAGE_KEY_STR: constants.USER_CONFLICT,
                }
            )
        return JsonResponse(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={
                    constants.MESSAGE_KEY_STR: constants.USER_CREATION_FAILURE
                }
            )
