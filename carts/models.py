from django.db import models

from general.model_mixins import UserMixin


class Cart(UserMixin,
           models.Model):
    """
    Пользователь добавляет товар в корзину.
    Пока поле order пустое, товар в корзине.
    Когда поле order непустое, это уже заказ.

    Таким образом организуется и текущая корзина,
    и история заказов.
    """

    product = models.ForeignKey("products.Product",
                                on_delete=models.CASCADE,
                                verbose_name="Товар")
    # Магазин торгует только штучными товарами.
    # Теоретически, возможна продажа весового товара (например, удобрений).
    # Но для интернет-магазина это довольно странно. А т.к. в ТЗ ничего не сказано,
    # поэтому трактуем самостоятельно: только штучный.
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
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзинах"
