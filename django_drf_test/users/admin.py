from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser


class CustomUserAdmin(UserAdmin):

    model = NewUser
    list_display = ['email', 'first_name', 'last_name', 'date_joined',]
    readonly_fields = ('date_joined',)


admin.site.register(NewUser, CustomUserAdmin)

