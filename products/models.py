from _decimal import Decimal


from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

from general.model_mixins import NameMixin


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

class ProductManager(models.Manager):
    def get_queryset(self):
        # В наличии и упорядоченные по убыванию даты добавления товара.
        return super().get_queryset().filter(stock__gte=1).order_by("-added")


class Product(NameMixin,
              models.Model):
    objects = models.Manager()  # По умолчанию. Нужен для админки.
    in_stock = ProductManager()

    added = models.DateTimeField(auto_now_add=True,
                                 verbose_name="Дата добавления")


    photo = models.ImageField(verbose_name="Фото. Рекомендовано 500 x 500 px", blank=False)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name="Цена",
                                validators=[MinValueValidator(Decimal('0.01'))])
    origin = models.ForeignKey(
        "Country",
        on_delete=models.CASCADE,
        verbose_name="Страна-производитель",
    )

    color = models.ForeignKey(
        "Color",
        on_delete=models.CASCADE,
        verbose_name="Цвет",
    )

    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        verbose_name="Категория / Вид товара",
    )

    stock = models.PositiveIntegerField(default=0,
                                        null=False,
                                        blank=False,
                                        verbose_name="Остаток товара")

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={"pk": self.id})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
