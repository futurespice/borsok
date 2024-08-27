from django.db import models
from menu.models import Dish
from promocodes.models import PromoCode
from django.utils import timezone

class Cart(models.Model):
    session_key = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    promo_code = models.ForeignKey(PromoCode, null=True, blank=True, on_delete=models.SET_NULL)

    @property
    def total_price(self):
        # Рассчитываем общую стоимость без учета скидок
        return sum(item.total_price for item in self.items.all())

    @property
    def total_price_with_discount(self):
        total = self.total_price
        if self.promo_code:
            discount = total * (self.promo_code.discount_percentage / 100)
            total -= discount
        return total

    def __str__(self):
        return f"Cart {self.id} - {self.session_key}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        base_price = self.dish.price
        promotion = self.dish.promotions.filter(is_active=True, start_date__lte=timezone.now(), end_date__gte=timezone.now()).first()
        if promotion:
            discount = base_price * (promotion.discount_percentage / 100)
            base_price -= discount
        return self.quantity * base_price

    def __str__(self):
        return f"{self.quantity} x {self.dish.name}"
