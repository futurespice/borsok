from django.urls import path
from .views import CategoryListView, CategoryCreateView, DishCreateView, DishesByCategoryView, CategoryListView, DishListView, DishSearchView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('dishes/', DishListView.as_view(), name='dish-list'),
    path('dishes/search/', DishSearchView.as_view(), name='dish-search'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<slug:slug>/dishes/', DishesByCategoryView.as_view(), name='dishes-by-category'),
    path('dishes/create/', DishCreateView.as_view(), name='dish-create'),
]
