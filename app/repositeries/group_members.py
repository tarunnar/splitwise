from app.models import GroupMembers


class GroupMembersRepository(object):

    @classmethod
    def get_group_members_by_filter(cls, filters):
        return GroupMembers.objects.filter(**filters)

    @classmethod
    def create_group_member(cls, group_id, user_id):
        return GroupMembers.objects.create(
            group_id=group_id,
            user_id=user_id
        )
