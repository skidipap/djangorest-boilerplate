from unicodedata import name
from django.urls import path, include
from allauth.account.views import ConfirmEmailView

from .views import GoogleLoginView

urlpatterns = [
    path('social/login', GoogleLoginView.as_view(), name="google_social_login"),

    # Django Allauth Confirm Email
    path('registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),

    # Django API Auth and Auth Route
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('', include('dj_rest_auth.urls')),
]