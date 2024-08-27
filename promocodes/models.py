from django.db import models

class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="Промокод")
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Процент скидки", default=0)
    expiration_date = models.DateTimeField(verbose_name="Дата окончания действия промокода")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return self.code

