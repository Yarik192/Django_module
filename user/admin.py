from django.contrib import admin
from user.models import UserProfile


@admin.register(UserProfile)
class AdminUserProfile(admin.ModelAdmin):
    pass
