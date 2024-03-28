from django.contrib import admin
from django.contrib.auth.models import Group
from core.models import UserData

admin.site.unregister(Group)
admin.site.register(UserData)
