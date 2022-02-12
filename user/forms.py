from django.contrib.auth import authenticate
from django import forms
from django.contrib.auth.models import User


class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(max_length=256)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError("Login or password incorrect")


class CustomRegistrationForm(forms.Form):
    username = forms.CharField(label="username", max_length=64)
    email = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            User.objects.get(username=username)
            raise forms.ValidationError("Username exist")
        except User.DoesNotExist:
            return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords don't match")
