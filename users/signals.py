from allauth.socialaccount.signals import social_account_added
from django.dispatch import receiver
from rest_framework_simplejwt.tokens import RefreshToken

@receiver(social_account_added)
def create_token_for_social_user(request, sociallogin, **kwargs):
    user = sociallogin.user
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    # Сохранение токена в сессии для дальнейшего использования
    request.session['access_token'] = access_token
    request.session['refresh_token'] = str(refresh)
