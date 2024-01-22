# Generated by Django 5.0.1 on 2024-01-22 19:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_alter_cart_order'),
        ('orders', '0001_initial'),
        ('products', '0006_alter_product_photo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='SelectedProduct',
        ),
        migrations.AlterModelOptions(
            name='selectedproduct',
            options={'verbose_name': 'Отобранный товар', 'verbose_name_plural': 'Отобранные товары'},
        ),
    ]
