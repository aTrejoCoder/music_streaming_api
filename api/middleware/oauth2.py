from django.contrib.auth import get_user_model
from django.utils import timezone
from oauth2_provider.models import Application, AccessToken
from django.conf import settings
import jwt

User = get_user_model()

def create_oauth2_token(user):
    """
    Create an OAuth2 access token for the given user.
    """
    application = Application.objects.get(name="oauth2_app")
    token = AccessToken.objects.create(
        user=user,
        application=application,
        expires=timezone.now() + timezone.timedelta(days=1),
        token=f"token_{user.user_id}_{timezone.now().timestamp()}"
    )
    return token