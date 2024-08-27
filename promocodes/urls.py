from django.urls import path
from .views import PromoCodeListView

urlpatterns = [
    path('promocodes/', PromoCodeListView.as_view(), name='promocode-list'),
]
