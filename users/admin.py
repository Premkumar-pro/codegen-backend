from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile

# Register CustomUser with the admin
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Display these fields in the list view
    list_display = ("id", "username", "full_name", "email", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")
    # Fields for add/edit forms
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("full_name", "email", "role")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "full_name", "email", "role", "password1", "password2", "is_staff", "is_active")}
        ),
    )
    search_fields = ("username", "full_name", "email")
    ordering = ("id",)

# Optional: Register UserProfile if you are using it
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "full_name", "email", "role", "created_at")
    search_fields = ("user__username", "full_name", "email")
