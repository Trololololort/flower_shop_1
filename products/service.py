from products.models import Product
from selected_products.service import get_cart_contents


def are_there_enough_products(user, product_id):
    """
    Нельзя добавить в корзину товаров больше, чем есть в наличии.
    Пользователь добавляет товар в корзину по одной штуке.

    Проверить, хватает ли товара с учетом того, что есть в корзине у этого
    пользователя.
    """
    product = Product.objects.filter(pk=product_id).first()
    all_products_in_cart = get_cart_contents(user)
    product_in_cart = all_products_in_cart.filter(product=product_id).values_list("quantity", flat=True)

    TO_BE_ORDERED = 1

    result = product.stock - TO_BE_ORDERED

    if product_in_cart:
        product_in_cart = product_in_cart[0]
        result -= product_in_cart

    return result >= 0