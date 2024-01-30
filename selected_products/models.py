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

    Назвать эту модель Cart - нееудачнай вариант.
    Причина: мы позже будем выводить содержание заказов,
    содержание корзины. И в заказе, и в корзине содержатся
    товары. Поэтому правильно не называть эту модель
    корзиной.
    """

    product = models.ForeignKey("products.Product",
                                on_delete=models.CASCADE,
                                verbose_name="Товар")

    # Магазин торгует только штучными товарами. Т.к. в ТЗ ничего не сказано,
    # трактуем самостоятельно: только штучный.

    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#positiveintegerfield
    ordered_quantity = models.PositiveIntegerField(blank=False,
                                                   null=False,
                                                   default=0,
                                                   verbose_name="Количество")


    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#foreignkey
    order = models.ForeignKey("orders.Order",
                              on_delete=models.CASCADE,
                              null=True,
                              blank=True, )

    # Декоратор @property в моделях Django помогает сделать код более чистым.
    # https://docs.python.org/3/library/functions.html#property
    @property
    def price(self):
        return self.product.price


    def total(self):
        return round(self.price * self.ordered_quantity, 2)


    def sum(self):
        return round(self.price * self.ordered_quantity, 2)

    # https://docs.djangoproject.com/en/5.0/ref/models/instances/#str
    def __str__(self):
        return self.product.name

    # https://docs.djangoproject.com/en/5.0/ref/models/options/
    class Meta:
        verbose_name = "Отобранный товар" # https://docs.djangoproject.com/en/5.0/ref/models/options/#verbose-name
        verbose_name_plural = "Отобранные товары" # https://docs.djangoproject.com/en/5.0/ref/models/options/#verbose-name-plural
