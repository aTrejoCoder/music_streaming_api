import graphene
from api.schema.types import UserType
from api.services.user_services import UserService
from api.utils import result
from api.utils.result import Result
from api.utils.api_response import UserResponse

class Query(graphene.ObjectType):
    get_user_by_id = graphene.Field(UserResponse, user_id=graphene.Int(required=True)) 
    all_users = graphene.List(UserType)

    def resolve_get_user_by_id(self, info, user_id):
        result = UserService.get_user_by_id(user_id)
        if result.is_failure():
            return UserResponse(success=False, message=result.get_error_msg(), user=None)
        
        return UserResponse(success=True, message="User retrieved successfully", user=result.get_data())

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()
