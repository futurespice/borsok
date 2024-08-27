from django.contrib import admin
from .models import Cart, CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'created_at')
    search_fields = ('session_key',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'dish', 'quantity')
    list_filter = ('cart',)
    search_fields = ('dish__name',)
