from django.contrib import admin

from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'phone', 'email', 'budget', 'created_at')
    search_fields = ('company', 'name', 'phone', 'email', 'category')
    list_filter = ('asset_type', 'budget', 'created_at')
