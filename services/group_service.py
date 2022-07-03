from models.group import Group
from services.group_service_interface import GroupServiceInterface


class GroupService(GroupServiceInterface):
    groups = dict()

    def add_group(self, _id, name, members):
        group = Group()
        group.set_group_id(_id)
        group.set_name(name)
        group.set_members(members)
        self.__class__.groups[_id] = group
        return group

    def register_member(self, _id, member):
        self.groups[_id].register_member(member)

    def de_register_member(self, _id, member):
        self.groups[_id].de_register_member(member)
