from django.shortcuts import get_object_or_404

from general.const import HttpStatusCodes
from selected_products.models import SelectedProduct
from products.models import Product


def get_cart_contents(user):
    """
    Корзина виртуальная.
    См. комментарий к модели selected_products.SelectedProduct.

    В корзине лежат отобранные пользователем товары,
    которым еще не создан заказ.
    """
    object_list = SelectedProduct.objects.filter(user=user).filter(order=None)

    return object_list


def add_product_to_cart(product_id, user, addend):
    """
    Корзина виртуальная.
    См. комментарий к модели selected_products.SelectedProduct.

    Получили ID продукта, пользователя и слагаемое.
    Слагаемое может быть 1 или -1. Т.е. добавляем или убираем
    из корзины одну единицу товара.

    Если в корзине ноль единиц данного товара, удалить такую запись
    из базы данных. Т.е. чтобы в корзине не было товаров, у которых количество
    нулевое.

    @param product_id: int
    @param user: CustomUser
    @param addend: int
    @return: dictionary, {status, message}
    """

    assert addend == 1 or addend == -1

    product = Product.in_stock.filter(pk=product_id).first()

    assert product is not None

    if product:

        the_product_already_in_cart = SelectedProduct.objects.filter(user=user, product=product, order=None).first()

        if the_product_already_in_cart:

            the_product_already_in_cart.ordered_quantity = (the_product_already_in_cart.ordered_quantity + addend)

            if the_product_already_in_cart.ordered_quantity == 0:
                the_product_already_in_cart.delete()  # https://docs.djangoproject.com/en/5.0/topics/db/queries/#deleting-objects
            else:
                the_product_already_in_cart.save()  # https://docs.djangoproject.com/en/5.0/ref/models/instances/#saving-objects

        else:
            SelectedProduct.objects.create(user=user, product=product, ordered_quantity=1)
        status = HttpStatusCodes.OK
    else:
        # Страховка. Не должны сюда попасть.
        status = HttpStatusCodes.WRONG_PRODUCT_ID


    return status


def get_message_whether_product_added_to_cart(http_status, addend):
    if http_status == HttpStatusCodes.OK:

        act = "добавлен в корзину" if addend > 0 else "убран из корзины"

        message = 'Товар {}.'.format(act)
    else:
        message = "Wrong product id"

    return message
