from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]
    # fieldsets = UserAdmin.fieldsets + (
    #     ('Contact Information', {
    #         "fields": (
    #             'phone_number',
    #         ),
    #     }),
    # )
    fieldsets = (
        ("Auth Info",{
            "fields": (
                'username',
                'email',
                'password',
            ),}),
        ("Personal Info",{
            "fields": (
                'first_name',
                'last_name',
                'phone_number',
            ),}),
        ("User permission",{
            
            "fields": (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        })
    )
     

admin.site.register(CustomUser, CustomUserAdmin)