from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
import users.views


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", users.views.SignUpView.as_view(), name="register")
]
