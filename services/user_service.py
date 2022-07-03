from models.user import User
from services.user_service_interface import UserServiceInterface


class UserService(UserServiceInterface):
    users = dict()

    def add_user(self, _id, name):
        user = User()
        user.set_user_id(_id)
        user.get_user_name(name)
        self.users[_id] = user
        return user
