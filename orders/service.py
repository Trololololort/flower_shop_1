from enum import Enum

from django.db import transaction

from selected_products.models import SelectedProduct
from orders.models import Order
from selected_products.service import get_cart_contents

"""
Правильно выполнять такие операции в транзакции.

Транзакция: либо все, либо ничего. 
Мы изменяем объекты двух моделей  Order и SelectedProduct.
Теоретически, возможна нештатная ситуация.
Если она возникнет, автоматически состояние базы данных вернется на 
момент до начала транзакции.

На демо-экзамене транзакции не будут оцениваться.
Поэтому в данном случае это просто вам на будущее.

Пример уместного применения транзакции: перевод
денег в банке. С покупателя списали деньги, что-то пошло не так,
до продавца деньги не дошли. 

Документация: https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic
"""
class ArithmeticOperation(Enum):
    PLUS = "+",
    MINUS = "i"

def adjust_stock(selected_products, arithmetic_operation):
    for selected_product in selected_products:
        if arithmetic_operation == ArithmeticOperation.MINUS:
            selected_product.product.stock = selected_product.product.stock - selected_product.ordered_quantity
        else:
            assert arithmetic_operation == ArithmeticOperation.PLUS
            selected_product.product.stock = selected_product.product.stock + selected_product.ordered_quantity

        if selected_product.product.stock < 0:
            raise Exception("Out of stock")

        selected_product.product.save()





@transaction.atomic
def create_order(user):
    """
    Создать заказ и обновить корзину (добавить значение для внешнего ключа - номер заказа).

    Возвращаем идентификатор вновь созданного заказа, чтобы в CreateOrderView
    создать сообщение пользователю, сославшись на этот номер.
    """
    selected_products = get_cart_contents(user)
    adjust_stock(selected_products, ArithmeticOperation.MINUS)
    new_order = Order.objects.create(user=user) # https://docs.djangoproject.com/en/5.0/topics/db/queries/#additional-methods-to-handle-related-objects

    selected_products.update(order=new_order) # https://docs.djangoproject.com/en/5.0/topics/db/queries/#updating-multiple-objects-at-once

    return new_order.pk

@transaction.atomic
def delete_order(order_id):
    # Не обрабатываем DoesNotExist,
    # позволяем исключению всплыть в вызывающий метод.
    order_obj = Order.objects.get(pk=order_id) # https://docs.djangoproject.com/en/5.0/topics/db/queries/#retrieving-a-single-object-with-get
    selected_products_in_order = order_obj.selectedproduct_set.all()
    adjust_stock(selected_products_in_order, ArithmeticOperation.PLUS)
    order_obj.delete() # https://docs.djangoproject.com/en/5.0/topics/db/queries/#deleting-objects


