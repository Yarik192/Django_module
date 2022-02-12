from django.contrib import admin
from django.utils.safestring import mark_safe

from user.models import UserProfile
# Register your models here.


@admin.register(UserProfile)
class AdminUserProfile(admin.ModelAdmin):
    list_display = ["user", "image_show", "balance"]

    def image_show(self, obj):
        if obj.avatar:
            return mark_safe("<img src='{}' width='60' />".format(obj.avatar.url))
        return "None"

    image_show.__name__ = "Картинка"
