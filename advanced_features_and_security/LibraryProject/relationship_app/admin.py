from django.contrib import admin
# WEEK 11
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# WEEK 11
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'date_of_birth', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)