from django.shortcuts import get_object_or_404

from carts.models import SelectedProduct
from products.models import Product


def get_cart_contents(user):
    """
    В корзине лежат товары пользователя,
    которым еще не создан заказ.
    """
    object_list = SelectedProduct.objects.filter(user=user).filter(order=None)

    return object_list

def add_product_to_cart(product_id, user, addend):
    product = Product.in_stock.filter(pk=product_id).first()

    assert product is not None

    if product:

        the_product_already_in_cart = SelectedProduct.objects.filter(user=user, product=product, order=None).first()

        if the_product_already_in_cart:
            the_product_already_in_cart.quantity = (the_product_already_in_cart.quantity + addend)

            if the_product_already_in_cart.quantity == 0:
                the_product_already_in_cart.delete()
            else:
                the_product_already_in_cart.save()

        else:
            SelectedProduct.objects.create(user=user, product=product, quantity=1)
        status = 200

        act = "добавлен в корзину" if addend > 0 else "убран из корзины"

        message = 'Товар "{}" {}.'.format(product.name, act)
    else:
        # Страховка. Не должны сюда попасть.
        status = 400
        message = "Wrong product id"

    return {"status": status, "message": message}