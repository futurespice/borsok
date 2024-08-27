from rest_framework import serializers
from .models import PromoCode

class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoCode
        fields = ['code', 'discount_percentage', 'expiration_date', 'is_active']
