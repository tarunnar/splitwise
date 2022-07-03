class Group(object):
    def __init__(self):
        self._id = None
        self._name = None
        self._members = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def set_group_id(self, id):
        self._id = id

    def set_members(self, members):
        self._members = members

    def get_group_id(self):
        return self._id

    def get_group_members(self):
        return self._members

    def register_member(self, member):
        self._members.append(member)

    def de_register_member(self, member):
        self._members.remove(member)