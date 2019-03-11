from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from apps.accounts.models import UserProfile

class MyOIDCAB(OIDCAuthenticationBackend):
    def create_user(self, claims):
        user = super(MyOIDCAB, self).create_user(claims)
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('last_name', '')
        user.username = claims.get('username', '')
        user.save()
        key = claims.get('access_key', '')
        profile = UserProfile.objects.create(access_key=key, user_id=user.id)
        return user

    def update_user(self, user, claims):
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('last_name', '')
        user.username = claims.get('username', '')
        user.save()
        key = claims.get('access_key', '')
        UserProfile.objects.filter(user_id=user.id).update(access_key=key)
        return user
