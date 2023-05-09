from .models import MyUser

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

UserAdmin.fieldsets += (
    ('Extra Fields', {'fields': ('bio',)}),
)
admin.site.register(MyUser, UserAdmin)
