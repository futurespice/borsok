from django.contrib import admin
from .models import PromoCode

@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percentage', 'expiration_date', 'is_active')
    list_filter = ('is_active', 'expiration_date')
    search_fields = ('code',)
