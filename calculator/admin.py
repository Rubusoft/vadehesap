from django.contrib import admin
from .models import InstallmentRate

@admin.register(InstallmentRate)
class InstallmentRateAdmin(admin.ModelAdmin):
    list_display = ('number_of_installments', 'interest_rate', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('number_of_installments', 'interest_rate')
    ordering = ('number_of_installments',)
