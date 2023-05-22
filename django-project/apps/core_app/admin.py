from django.contrib import admin
from django.utils import timezone


class BaseAdmin(admin.ModelAdmin):

    @staticmethod
    def logical_deleter(request, queryset):
        queryset.update(deleted_at=timezone.now())
        queryset.update(is_deleted=True)
        queryset.update(is_active=False)

    @staticmethod
    def deactivate(request, queryset):
        queryset.update(is_active=False)

    @staticmethod
    def activate(request, queryset):
        queryset.update(is_active=True)

    @staticmethod
    def undelete(request, queryset):
        queryset.update(is_deleted=False)
        queryset.update(deleted_at=None)
        queryset.update(is_active=True)

    actions = ['logical_deleter', 'deactivate', 'activate', 'undelete']
