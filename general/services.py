def get_total(a_queryset):
    """
    Получает выборку товаров, подсчитывает их сумму.

    Применяется для подсчета общей суммы:
    1) Лежащих в корзине товаров.
    2) Заказа.
    """
    sum = 0
    [sum := sum + elem.product.price * elem.quantity for elem in a_queryset]
    return sum
