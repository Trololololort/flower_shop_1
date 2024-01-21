from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from orders.models import Order
from orders.service import create_order


class CreateOrder(LoginRequiredMixin,
                  View):

    def post(self, request):

        user = request.user
        password = request.POST.get("password")

        try:
            validate_password(password=password, user=user)
        except ValidationError:
            messages.add_message(request, messages.ERROR, "Неверный пароль")
            return redirect("cart-detail")

        new_order_id = create_order(user)

        messages.add_message(request, messages.INFO, "Ваш заказ номер {} принят к исполнению.".format(new_order_id))

        return redirect("orders-list")


class OrdersListView(LoginRequiredMixin,
                     ListView):
    model = Order
