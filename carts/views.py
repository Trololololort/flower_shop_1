from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from carts.service import add_product_to_cart, get_cart_contents


class AddToCart(LoginRequiredMixin,
                View):
    def post(self, request):
        """
        Добавить или убрать товар из корзины.
        Если товар не может быть добавлен в корзину, сообщить об этом.

        product_id - id товара.
        addend - может быть +1 (добавить) или -1 (удалить).

        Товар можно добавить из каталога, карточки товара и из корзины.
        Т.е. из разных мест.
        Поэтому сообщение показать на странице, где добавлялся товар.
        """
        product_id = request.POST.get('product_id')
        addend = int(request.POST.get('addend'))

        assert (addend == 1 or addend == -1)

        status = add_product_to_cart(product_id, request.user, addend)

        if status["status"] == 200:
            messages.add_message(request, messages.INFO, status["message"])
            return redirect(request.META['HTTP_REFERER'])
        else:
            return HttpResponse(status["message"], status=status["status"])


def get_total(a_queryset):
    sum = 0
    [sum := sum + elem.product.price * elem.quantity for elem in a_queryset]
    return sum

class CartDetailView(LoginRequiredMixin,
                     TemplateView):
    template_name = "carts/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = get_cart_contents(self.request.user)
        context["object_list"] = object_list
        context["total"] = get_total(object_list)
        return context

