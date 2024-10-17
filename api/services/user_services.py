from api.models import User
from api.utils.result import Result
from django.contrib.auth.hashers import make_password


class UserService:
    def validate_user_credentials(email, username):
        if User.objects.filter(email=email):
            return Result.error("email already taken")
        elif User.objects.filter(username=username):
            return Result.error("username already taken")
        else:
            return Result.success(None)

    def get_user_by_username(username):
        try:
            user = User.objects.get(username=username)

            return Result.success(user)
        except User.DoesNotExist:
            return Result.error(f"user with id {username} not found")

    def get_user_by_email(email):
        try:
            user = User.objects.get(email=email)

            return Result.success(user)
        except User.DoesNotExist:
            return Result.error(f"user with id {email} not found")


    def get_user_by_id(user_id):
        try:
            user = User.objects.get(user_id=user_id)
            return Result.success(user)
        except User.DoesNotExist:
            return Result.error(f"user with id {user_id} not found")


    def create_user(data):
        user = User(
            email=data.get('email'),
            username=data.get('username'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name')
            
        )
        user.set_password(data.get('password'))
        user.save()
        return user 
    
    def update_user(data):
        try:
            user_id = data.get('user_id')
            if not user_id:
                return Result.error("User ID is required")

            user = User.objects.get(user_id=user_id)

            if data.get('email'):
                user.email = data.get('email')
            if data.get('username'):
                user.username = data.get('username')
            if data.get('first_name'):
                user.first_name = data.get('first_name')
            if data.get('last_name'):
                user.last_name = data.get('last_name')
            if data.get('password'):
                user.set_password(data.get('password')) 
                
            user.save()
            return Result.success(user)

        except User.DoesNotExist:
            return Result.error(f"user with id {user_id} not found")


    def delete_user(user_id):
        try:
            user = User.objects.get(user_id=user_id)
            user.delete()
            return Result.success(None)
        except User.DoesNotExist:
            return Result.error(f"user with id {user_id} not found")
