class GroupController:
    def __init__(self, group_service_interface):
        self.group_service_interface = group_service_interface

    def add_group(self, _id, name, members):
        return self.group_service_interface.add_group(_id, name, members)
