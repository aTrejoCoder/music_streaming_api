from api.models import User
from django.conf import settings
from api.middleware.oauth2 import create_oauth2_token
from api.middleware.jwt import generate_jwt_token
from api.services.user_services import UserService
from api.utils.result import Result

from api.models import User
from api.services.user_services import UserService
from api.utils.result import Result

class AuthService:
    def validate_login_credentials(identifier_value, password):
        """
        Authenticate a user based on email or username and return user object if successful,
        or None otherwise.
        """
        try:
            email_result = UserService.get_user_by_email(identifier_value)
            
            if email_result.is_success():
                user = email_result.get_data()
                
                if user.check_password(password):
                    return Result.success(user)
                else:
                    return Result.error("Invalid password")

            username_result = UserService.get_user_by_username(identifier_value)
            if username_result.is_success():
                user = username_result.get_data()
                
                if user.check_password(password):
                    return Result.success(user)
                else:
                    return Result.error("Invalid password")
            
            return Result.error("User not found")
        except User.DoesNotExist:
            return Result.error("User does not exist")


    def procces_login(user):
        """
        proccess login a user and return JWT and OAuth2 tokens.
        """
        if user:
            jwt_token = generate_jwt_token(user)
            oauth2_token = create_oauth2_token(user)
            return {
                'jwt_token': jwt_token,
                'oauth2_token': oauth2_token.token,
                'user': user
            }
        return None


    def signup_user(user_data):
        """
        Create a new user and return JWT and OAuth2 tokens.
        """
        user = UserService.create_user(user_data)
        
        jwt_token = generate_jwt_token(user)
        oauth2_token = create_oauth2_token(user)

        return {
            'jwt_token': jwt_token,
            'oauth2_token': oauth2_token.token,
            'user': user
        }