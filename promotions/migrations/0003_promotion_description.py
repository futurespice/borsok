# Generated by Django 5.1 on 2024-08-27 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0002_rename_title_promotion_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
