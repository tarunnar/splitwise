class UserController:
    def __init__(self, user_service_interface):
        self.user_service_interface = user_service_interface

    def add_user(self, _id, _name):
        return self.user_service_interface.add_user(_id, _name)
