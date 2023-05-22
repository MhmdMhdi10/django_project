from django.contrib import admin

from apps.core_app.admin import BaseAdmin
from .models import UserProfile, Address


@admin.register(Address)
class AddressAdmin(BaseAdmin):
    list_display = ('body', 'city', 'created', 'last_updated', 'deleted_at', 'restored_at', 'is_deleted', 'is_active')
    list_filter = ('is_deleted', 'is_active')
    search_fields = ('body', 'city')


@admin.register(UserProfile)
class UserProfileAdmin(BaseAdmin):
    list_display = ('user', 'phone', 'address',
                    'created', 'last_updated', 'deleted_at', 'restored_at', 'is_deleted', 'is_active')
    list_filter = ('is_deleted', 'is_active')
    search_fields = ('user__email', 'user__phone_number', 'phone')