import jwt
from django.conf import settings
from django.http import JsonResponse
from jwt import ExpiredSignatureError, InvalidTokenError

def generate_jwt_token(user):
    """
    Generate a JWT token for the given user.
    """
    payload = {
        'user_id': user.user_id,
        'exp': timezone.now() + timezone.timedelta(days=1),
        'iat': timezone.now()
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')


def get_user_id_from_request(request):
    """
    Function to extract the JWT token from the Authorization header,
    decode it, and return the user_id.
    """
    auth_header = request.headers.get('Authorization')
    
    if not auth_header:
        return JsonResponse({"error": "Authorization header is missing"}, status=401)

    # Check if the token is a Bearer token
    if not auth_header.startswith('Bearer '):
        return JsonResponse({"error": "Invalid token header. No 'Bearer' keyword found"}, status=401)

    token = auth_header.split(' ')[1]

    try:
        # Decode the JWT token
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_id = payload.get('user_id')

        if user_id is None:
            return JsonResponse({"error": "Invalid token: user_id not found"}, status=401)

        return user_id

    except ExpiredSignatureError:
        return JsonResponse({"error": "Token has expired"}, status=401)

    except InvalidTokenError:
        return JsonResponse({"error": "Invalid token"}, status=401)
