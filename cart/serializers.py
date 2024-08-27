from rest_framework import serializers
from .models import Cart, CartItem
from menu.serializers import DishSerializer
from promocodes.models import PromoCode

class CartItemSerializer(serializers.ModelSerializer):
    dish = DishSerializer()
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = CartItem
        fields = ['id', 'dish', 'quantity', 'total_price']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    total_price_with_discount = serializers.ReadOnlyField()
    promo_code = serializers.CharField(source='promo_code.code', allow_null=True, required=False)

    class Meta:
        model = Cart
        fields = ['id', 'items', 'created_at', 'total_price_with_discount', 'promo_code']
