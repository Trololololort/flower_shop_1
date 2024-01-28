import uuid

from django.db import models
from django.db.models import Sum
from django.urls import reverse

from general.model_mixins import UserMixin
from orders.const import ORDER_STATUS


class Order(UserMixin,
            models.Model):
    ordered_at = models.DateTimeField(auto_now_add=True, # https://docs.djangoproject.com/en/5.0/ref/models/fields/#datetimefield
                                      verbose_name="Дата заказа")

    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#charfield
    status = models.CharField(max_length=9,
                              choices=ORDER_STATUS, # https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices
                              verbose_name="Статус",
                              blank=True,
                              null=False,
                              default="NEW")

    cancellation_cause = models.TextField(verbose_name="Причина отказа", # https://docs.djangoproject.com/en/5.0/ref/models/fields/#textfield
                                          default="",
                                          null=False,
                                          blank=True)

    def ordered_by(self):
        # Для админки: по ТЗ в списке видно ФИО заказчика.
        return self.user.full_name

    ordered_by.short_description = 'ФИО заказчика' # https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#the-display-decorator

    def number_of_ordered_products(self):
        # Для админки: по ТЗ в списке видно количество заказанных товаров.
        # https://docs.djangoproject.com/en/5.0/topics/db/aggregation/#aggregating-on-empty-querysets-or-groups
        return self.selectedproduct_set.aggregate(number_of_products=Sum("quantity")).get("number_of_products")

    number_of_ordered_products.short_description = 'Количество заказанных товаров' # https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#the-display-decorator

    def get_absolute_url(self):
        # https://docs.djangoproject.com/en/5.0/ref/models/instances/#get-absolute-url
        return reverse('order-detail', kwargs={"pk": self.id})

    def __str__(self): # https://docs.djangoproject.com/en/5.0/ref/models/instances/#str
        return "{}".format(self.id) # https://docs.djangoproject.com/en/5.0/ref/models/instances/#str

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
