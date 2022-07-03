from ..controllers.user_controller import UserController
from ..controllers.group_controller import GroupController
from ..controllers.bill_controller import BillController

from ..services.bill_service import BillService
from ..services.user_service import UserService
from ..services.group_service import GroupService

user_service = UserService()
bill_service = BillService()
group_service = GroupService()
user_controller = UserController(user_service)
group_controller = GroupController(group_service)
bill_controller = BillController(group_service)
print(user_controller)

