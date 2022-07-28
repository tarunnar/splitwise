from MySQLdb import IntegrityError
from app.models import User
from rest_framework.authtoken.models import Token
import logging
import traceback

logger = logging.getLogger(__name__)


class UserSrvice(object):
    success_status = 1
    failure_status = 0
    conflict_status = 2

    @classmethod
    def create_user(cls, email, password, name):
        try:
            User.objects.get(email=email)
            return {
                "status": cls.conflict_status,
                "user": None
            }
        except Exception as exc:
            user = User.objects.create_user(email=email, password=password, name=name)
            token = Token.objects.create(user=user)
            return {
                "status": cls.success_status,
                "user": user,
                "token": token.key
            }