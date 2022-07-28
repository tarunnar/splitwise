from django.shortcuts import redirect
from rest_framework import exceptions
from rest_framework.authtoken.models import Token

from app import constants


class AuthMixin(object):
    def dispatch(self, request, *args, **kwargs):
        headers = request.headers
        token = headers.get("token")
        if not token:
            raise exceptions.NotAuthenticated({
                constants.MESSAGE_KEY_STR: constants.AUTH_TOKEN_MISSING
            })

        try:
            token_obj = Token.objects.get(key=token)
            user_id = token_obj.user

        except:
            raise exceptions.NotAuthenticated({
                    constants.MESSAGE_KEY_STR: constants.INVALID_TOKEN
            })
        kwargs["user_id"] = user_id
        return super(AuthMixin, self).dispatch(request, *args, **kwargs)
