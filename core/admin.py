from django.contrib import admin
from django.contrib.auth.models import Group
from core.models import UserData


class UserDataAdmin(admin.ModelAdmin):
    list_display = ["ip", "browser", "click_time"]


admin.site.unregister(Group)
admin.site.register(UserData, UserDataAdmin)
