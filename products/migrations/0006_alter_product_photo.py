# Generated by Django 5.0.1 on 2024-01-21 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_goods_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='', verbose_name='Фото. Рекомендовано 500 x 500 px'),
        ),
    ]
