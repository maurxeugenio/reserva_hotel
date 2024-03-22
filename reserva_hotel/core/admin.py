from django.contrib import admin
from .models import Profile, User, Company
from django.contrib.auth.admin import UserAdmin


admin.site.register([Profile, Company])


class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'active_company']
    list_editable = ['active_company']


admin.site.register(User, CustomUserAdmin)