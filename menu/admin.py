from django.contrib import admin
from .models import Category, Dish

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Убираем 'description', так как этого поля больше нет
    search_fields = ('name',)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_special_offer')
    list_filter = ('category', 'is_special_offer')
    search_fields = ('name',)
