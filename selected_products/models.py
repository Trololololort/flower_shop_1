from django.db import models

from general.model_mixins import UserMixin


class SelectedProduct(UserMixin,
                      models.Model):
    """
    Корзины как сущности нет.
    Пользователь отобрал товар.
    Пока поле order пустое, товар в корзине.
    Когда поле order непустое, это уже
    совершенный заказ.
    Т.е. корзина виртуальная.
    """

    product = models.ForeignKey("products.Product",
                                on_delete=models.CASCADE,
                                verbose_name="Товар")

    # Магазин торгует только штучными товарами. Т.к. в ТЗ ничего не сказано,
    # трактуем самостоятельно: только штучный.
    quantity = models.PositiveIntegerField(blank=False,
                                           null=False,
                                           default=0,
                                           verbose_name="Количество")

    order = models.ForeignKey("orders.Order",
                              on_delete=models.CASCADE,
                              null=True,
                              blank=True, )

    def price(self):
        return self.product.price

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name = "Отобранный товар"
        verbose_name_plural = "Отобранные товары"
