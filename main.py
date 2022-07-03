from controllers.user_controller import UserController
from controllers.group_controller import GroupController
from controllers.bill_controller import BillController

from services.bill_service import BillService
from services.user_service import UserService
from services.group_service import GroupService

user_service = UserService()
bill_service = BillService()
group_service = GroupService()
user_controller = UserController(user_service)
group_controller = GroupController(group_service)
bill_controller = BillController(bill_service)
user1 = user_controller.add_user("user1", "tarun")
user2 = user_controller.add_user("user2", "pankaj")
user3 = user_controller.add_user("user3", "suresh")
user4 = user_controller.add_user("user4", "amit")

group = group_controller.add_group("group1", "kktrip", [user1, user2, user3, user4])

bill = bill_controller.add_bill("coffee", user1, "group1", {user1: 25, user2: 25, user3: 30, user4: 20}, 200)

balances = bill_controller.get_group_balance("group1")
print(balances)



