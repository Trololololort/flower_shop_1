from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView

from general.const import HttpStatusCodes
from selected_products.service import get_cart_contents, add_product_to_cart, get_message_whether_product_added_to_cart
from general.services import get_total
from orders.forms import OrderForm


class AddToCart(LoginRequiredMixin,
                # https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-loginrequiredmixin-mixin
                View):  # https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#view
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
        message = get_message_whether_product_added_to_cart(http_status=status, addend=addend)

        if status == HttpStatusCodes.OK:
            messages.add_message(request,
                                 messages.INFO,
                                 message)  # https://docs.djangoproject.com/en/5.0/ref/contrib/messages/

            # В запросе всегда содержится адрес страницы, отправившей его.
            # В корзину добавляться товар может с разных страниц (из каталога, из з карточки товара и из корзины).
            # Вернем ответ адресату запроса.
            return redirect(
                request.META['HTTP_REFERER'])  # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#redirect
        else:
            return HttpResponse(message,
                                status=status.value)  # https://docs.djangoproject.com/en/5.0/ref/request-response/#httpresponse-objects


class CartDetailView(LoginRequiredMixin,
                     # https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-loginrequiredmixin-mixin
                     TemplateView):  # https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#templateview
    template_name = "selected_products/cart.html"  # https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#templateview

    def get_context_data(self,
                         **kwargs):  # https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#templateview
        context = super().get_context_data(**kwargs)
        object_list = get_cart_contents(self.request.user)
        context["object_list"] = object_list
        context["order_form"] = OrderForm()
        context["grand_total"] = get_total(object_list)
        return context
