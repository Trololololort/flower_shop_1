from _decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

from general.model_mixins import NameMixin


class ProductManager(models.Manager):
    # https://docs.djangoproject.com/en/5.0/topics/db/managers/#custom-managers
    # https://docs.djangoproject.com/en/5.0/topics/db/managers/#modifying-a-manager-s-initial-queryset
    def get_queryset(self):
        # В наличии и упорядоченные по убыванию даты добавления товара.
        return super().get_queryset().filter(stock__gte=1).order_by("-added_at")


class Product(NameMixin,
              models.Model):
    objects = models.Manager()  # По умолчанию. Нужен для админки.
    in_stock = ProductManager() # https://docs.djangoproject.com/en/5.0/topics/db/managers/#custom-managers

    added_at = models.DateTimeField(auto_now_add=True, # https://docs.djangoproject.com/en/5.0/ref/models/fields/#datetimefield
                                    verbose_name="Дата добавления")

    photo = models.ImageField(verbose_name="Фото. Рекомендовано 500 x 500 px", blank=False) # https://docs.djangoproject.com/en/5.0/ref/models/fields/#imagefield
    price = models.DecimalField(max_digits=10, # https://docs.djangoproject.com/en/5.0/ref/models/fields/#decimalfield
                                decimal_places=2,
                                verbose_name="Цена",
                                validators=[MinValueValidator(Decimal('0.01'))])

    origin = models.ForeignKey( # https://docs.djangoproject.com/en/5.0/ref/models/fields/#foreignkey
        "product_properties.Country",
        on_delete=models.CASCADE,
        verbose_name="Страна-производитель",
    )

    color = models.ForeignKey( # https://docs.djangoproject.com/en/5.0/ref/models/fields/#foreignkey
        "product_properties.Color",
        on_delete=models.CASCADE,
        verbose_name="Цвет",
    )

    category = models.ForeignKey( # https://docs.djangoproject.com/en/5.0/ref/models/fields/#foreignkey
        "product_properties.Category",
        on_delete=models.CASCADE,
        verbose_name="Категория / Вид товара",
    )

    stock = models.PositiveIntegerField(default=0, #https://docs.djangoproject.com/en/5.0/ref/models/fields/#positivebigintegerfield
                                        null=False,
                                        blank=False,
                                        verbose_name="Остаток товара")

    def get_absolute_url(self):
        # https://docs.djangoproject.com/en/5.0/ref/models/instances/#get-absolute-url
        return reverse('product-detail', kwargs={"pk": self.id})

    class Meta:
        verbose_name = "Товар" # https://docs.djangoproject.com/en/5.0/ref/models/options/#verbose-name
        verbose_name_plural = "Товары" # https://docs.djangoproject.com/en/5.0/ref/models/options/#verbose-name-plural
