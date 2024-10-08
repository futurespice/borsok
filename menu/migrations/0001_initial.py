# Generated by Django 5.1 on 2024-08-23 23:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('description', models.TextField(blank=True, verbose_name='Описание категории')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название блюда')),
                ('description', models.TextField(blank=True, verbose_name='Описание блюда')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='dishes/', verbose_name='Изображение блюда')),
                ('is_special_offer', models.BooleanField(default=False, verbose_name='Специальное предложение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='menu.category', verbose_name='Категория')),
            ],
        ),
    ]
