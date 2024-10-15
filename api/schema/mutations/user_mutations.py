import graphene
import datetime
from api.services.user_services import UserService
from api.schema.types import UserType
from api.utils.api_response import UserResponse
from api.utils.result import Result


class CreateUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    response = graphene.Field(UserResponse)

    def mutate(self, info, email, username, password, first_name, last_name):
        validation_result = UserService.validate_user_credentials(email, username)

        if validation_result.is_failure():
            return CreateUser(
                response=UserResponse(
                    success=False,
                    user=None,
                    message=validation_result.get_error_msg(),
                )
            )

        user_data = {
            'email': email,
            'username': username,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
        }

        user = UserService.create_user(user_data)

        return CreateUser(
            response=UserResponse(
                success=True,
                user=user,
                message="User created successfully"
            )
        )


class UpdateUser(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int(required=True)
        email = graphene.String()
        username = graphene.String()
        password = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()

    response = graphene.Field(UserResponse)

    def mutate(self, info, user_id, email=None, username=None, password=None, first_name=None, last_name=None):
        user_data = {
            'user_id': user_id,
            'email': email,
            'username': username,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
        }

        result = UserService.update_user(user_data)
        
        if result.is_failure():
            return DeleteUser(response=UserResponse(
                success=False,
                user=None,
                message=result.get_error_msg(),
            ))     

        return UpdateUser(response=UserResponse(
                success=True,
                user=result.get_data(),
                message="User updated successfully"
            ),
        )

class DeleteUser(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int(required=True)

    response = graphene.Field(UserResponse)

    def mutate(self, info, user_id):
        result = UserService.delete_user(user_id)
        if result.is_failure():
            return DeleteUser(response=UserResponse(
                success=False,
                user=None,
                message=result.get_error_msg(),
            ))
        
        return DeleteUser(
            response=UserResponse(
                success=True,
                user=None,
                message="User deleted successfully"
            ),
        )
