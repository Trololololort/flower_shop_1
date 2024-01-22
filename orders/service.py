from django.db import transaction

from carts.models import SelectedProduct
from orders.models import Order


@transaction.atomic
def create_order(user):
    """
    Создать заказ и обновить корзину (добавить значение для внешнего ключа - номер заказа).

    """
    carts = SelectedProduct.objects.filter(user=user, order=None)

    new_order = Order.objects.create(user=user)

    carts.update(order=new_order)

    return new_order.pk