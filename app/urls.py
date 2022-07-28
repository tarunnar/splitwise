from django.urls import path
from app.views.user import UserView
from app.views.group import GroupView
from app.views.group_members import GroupMembersView
from app.views.bill import BillView
from app.views.group_balances import GroupBalancesView
from app.views.group_user_balances_view import GroupUserBalancesView


urlpatterns = [
    path('user/create_user/', UserView.as_view()),
    path('user/create_group/', GroupView.as_view()),
    path('group_members/', GroupMembersView.as_view()),
    path('bills/', BillView.as_view()),
    path('group_balances/', GroupBalancesView.as_view()),
    path('user_balances/', GroupUserBalancesView.as_view()),
]
