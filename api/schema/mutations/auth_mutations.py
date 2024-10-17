import graphene
from api.services.user_services import UserService
from api.services.auth_service import AuthService
from api.schema.types import UserType
from api.utils.result import Result
from api.utils.api_response import AuthResponse

from graphql_jwt.decorators import login_required


class SignUpMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    response = graphene.Field(AuthResponse)

    def mutate(self, info, email, username, password, first_name, last_name):
        validation_result = UserService.validate_user_credentials(email, username)
        if validation_result.is_failure():
            return SignUpMutation(
                response=AuthResponse(
                success=False,
                jwt_token=None,
                oauth2_token=None,
                user =None,
                message=validation_result.get_error_msg()
            )
        )

        user_data = {
            'email': email,
            'username': username,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
        }

        signupData = AuthService.signup_user(user_data)

        return SignUpMutation(
            response=AuthResponse(
                success=True,
                jwt_token=signupData.get('jwt_token'),
                oauth2_token=signupData.get('oauth2_token'),
                user = signupData.get('user'),
                message="Signup successfully proccesed"
            )
        )


class LoginMutation(graphene.Mutation):
    class Arguments:
        # email or username
        identifier_value = graphene.String(required=True)
        password = graphene.String(required=True)

    response = graphene.Field(AuthResponse)

    def mutate(self, info, identifier_value, password):
        validation_result = AuthService.validate_login_credentials(identifier_value, password)
        if validation_result.is_failure():
            return LoginMutation(
                response=AuthResponse(
                    success=False,
                    jwt_token=None,
                    oauth2_token=None,
                    user=None,
                    message=validation_result.get_error_msg(),
                )
            )

        login_data = AuthService.procces_login(validation_result.get_data())
        return LoginMutation(
            response=AuthResponse(
                success=True,
                jwt_token=login_data.get('jwt_token'),
                oauth2_token=login_data.get('oauth2_token'),
                user=login_data.get('user'),
                message="Login successfully processed"
            )
        )

class Query(graphene.ObjectType):
    me = graphene.Field(UserType)

    @login_required
    def resolve_me(self, info):
        return info.context.user

class Mutation(graphene.ObjectType):
    sign_up = SignUpMutation.Field()
    login = LoginMutation.Field()