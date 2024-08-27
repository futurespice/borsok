from django.urls import path
from .views import CartView, AddToCartView, RemoveFromCartView, DecreaseCartItemView, IncreaseCartItemView, ApplyPromoCodeView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/<int:id>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('cart/decrease/<int:id>/', DecreaseCartItemView.as_view(), name='decrease-cart-item'),
    path('cart/increase/<int:id>/', IncreaseCartItemView.as_view(), name='increase-cart-item'),
    path('cart/apply-promo/', ApplyPromoCodeView.as_view(), name='apply-promo-code'),
]
