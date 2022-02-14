from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CustomUserCreationForm


# def register_view(request: HttpRequest) -> HttpResponse:
#     if request.method == "POST":
#         form = CustomRegistrationForm(request.POST)
#         if form.is_valid():
#             User.objects.create_user(
#                 username=form.cleaned_data.get("username"),
#                 email=form.cleaned_data.get("email"),
#                 password=form.cleaned_data.get("password2")
#             )
#             return HttpResponseRedirect("/")
#     if request.method == "GET":
#         form = CustomRegistrationForm
#     return render(request, "registration/register.html", {"form": form})

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()