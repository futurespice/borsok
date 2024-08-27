from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Dish(models.Model):
    category = models.ForeignKey(Category, related_name='dishes', on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=255, verbose_name="Название блюда")
    description = models.TextField(blank=True, verbose_name="Описание блюда")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='dishes/', blank=True, null=True, verbose_name="Изображение блюда")
    is_special_offer = models.BooleanField(default=False, verbose_name="Специальное предложение")

    def __str__(self):
        return self.name
