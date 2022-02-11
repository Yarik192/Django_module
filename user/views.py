from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def register_view(request: HttpRequest) -> HttpResponse:
    ...


def login_view(request: HttpRequest) -> HttpResponse:
    return render(request, "user/login.html")


def logout_view(request: HttpRequest) -> HttpResponse:
    ...
