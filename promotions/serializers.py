from rest_framework import serializers
from .models import Promotion
from menu.serializers import DishSerializer

class PromotionSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)

    class Meta:
        model = Promotion
        fields = ['id', 'name', 'description', 'discount_percentage', 'dishes', 'start_date', 'end_date']
