from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class FasthomeUserAdmin(UserAdmin):

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "phone",
        "is_staff",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        "is_phone_verified",
    )

    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "phone",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Informations Fasthome",
            {
                "fields": (
                    "phone",
                    "city",
                    "is_phone_verified",
                    "is_profile_completed",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )