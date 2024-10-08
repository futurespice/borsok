# Generated by Django 5.1 on 2024-08-23 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Промокод')),
                ('discount_percentage', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Процент скидки')),
                ('expiration_date', models.DateTimeField(verbose_name='Дата окончания действия промокода')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
        ),
    ]
