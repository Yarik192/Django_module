from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
import user.views


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", user.views.register_view, name="register")
]
