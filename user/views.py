from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from user.models import UserProfile
from user.forms import CustomRegistrationForm


def register_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data.get("username"),
                email=form.cleaned_data.get("email"),
                password=form.cleaned_data.get("password2"))
            UserProfile.objects.create()
            return HttpResponseRedirect("/")
    if request.method == "GET":
        form = CustomRegistrationForm
    return render(request, "registration/login.html", {"form": form})
