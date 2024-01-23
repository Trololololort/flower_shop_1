from django.db import models

from general.model_mixins import NameMixin


# Create your models here.
class Country(NameMixin,
              models.Model):
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Category(NameMixin,
               models.Model):
    class Meta:
        verbose_name = "Категория/Вид товара"
        verbose_name_plural = "Категории/Виды товаров"


class Color(NameMixin,
            models.Model):
    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"
