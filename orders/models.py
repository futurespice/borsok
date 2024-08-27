from django.db import models

# Create your models here.
from django.db import models
from cart.models import Cart


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидается'),
        ('processing', 'В обработке'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменен'),
    ]

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders')
    address = models.CharField(max_length=255, verbose_name="Адрес доставки")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.get_status_display()}"

    @property
    def total_price(self):
        return self.cart.total_price_with_discount
