class User(object):
    def __init__(self):
        self._id = None
        self._name = None

    def set_user_id(self, id):
        self._id = id

    def set_user_name(self, name):
        self._name = name

    def get_user_id(self):
        return self._id

    def get_user_name(self, name):
        return self._name

    def __repr__(self):
        return str(self._id)