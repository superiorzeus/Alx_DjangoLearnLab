from django.contrib import admin
from .models import Book

# WEEK_11
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser # Import your CustomUser model

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

# WEEK_11
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # list_display, search_fields, and ordering to include new fields and manage username/email
    list_display = ['email', 'username', 'first_name', 'last_name', 'date_of_birth', 'is_staff']
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',) # You can choose 'username' or 'email'

    # Extend default fieldsets to include new fields
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)