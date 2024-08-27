from django.db import models
from menu.models import Dish  # Импорт модели блюд


class Promotion(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название акции")
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Процент скидки", default=0)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    start_date = models.DateTimeField(verbose_name="Дата начала акции")
    end_date = models.DateTimeField(verbose_name="Дата окончания акции")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    dishes = models.ManyToManyField(Dish, related_name='promotions', blank=True, verbose_name="Блюда в акции")

    def __str__(self):
        return self.name
