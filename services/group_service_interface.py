import abc


class GroupServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_group(self, _id, name, members):
        pass

    @abc.abstractmethod
    def register_member(self, _id, member):
        pass

    @abc.abstractmethod
    def de_register_member(self, _id, member):
        pass

