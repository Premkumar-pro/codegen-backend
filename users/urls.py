from django.urls import path
from .views import signup_api, login_api, dashboard, check_auth, github_login

urlpatterns = [
    path('signup/', signup_api),
    path('login/', login_api),
    path('dashboard/', dashboard),
    path('check-auth/', check_auth),
    path('github-login/', github_login),  # only login page
]
