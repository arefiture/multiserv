import jwt
from rest_framework.authentication import BaseAuthentication
from django.conf import settings
from rest_framework import exceptions


class ECAAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization', '')
        
        if not auth_header.startswith('Bearer '):
            return None

        try:
            token = auth_header.split()[1]
            payload = jwt.decode(
                token,
                settings.ECA_PUBLIC_KEY,  # Используем публичный ключ
                algorithms=['RS256'],     # Указываем алгоритм
                options={'verify_exp': True}
            )
            
            user = type('User', (), {
                'id': payload.get('user_id'),
                'username': payload.get('username'),
                'is_authenticated': True
            })()
            
            return (user, None)

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token expired')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid token')
        except Exception as e:
            raise exceptions.AuthenticationFailed(str(e))
