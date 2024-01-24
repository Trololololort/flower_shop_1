from django.contrib import messages, auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Model
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView

from general.services import get_total
from orders.models import Order
from orders.service import create_order, delete_order


class CreateOrder(LoginRequiredMixin,
                  View):
    def post(self, request):
        user = request.user
        password = request.POST.get("password")

        password_correct_for_user = auth.authenticate(request, username=user.username, password=password)

        if not password_correct_for_user:
            messages.add_message(request, messages.ERROR, "Неверный пароль")
            return redirect("cart-detail")

        new_order_id = create_order(user)

        messages.add_message(request, messages.INFO, "Ваш заказ номер {} принят к исполнению.".format(new_order_id))

        return redirect("orders-list")


class OrdersListView(LoginRequiredMixin,
                     ListView):
    model = Order

    def get_queryset(self):
        result = Order.objects.filter(user=self.request.user).order_by(
            "-ordered_at")
        return result


class OrderDetailView(LoginRequiredMixin,
                      DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.object.selectedproduct_set.all()
        context["total"] = get_total(context["object_list"])
        return context


class DeleteOrder(LoginRequiredMixin,
                  View):

    def post(self, request):
        order_id = request.POST.get("order")

        try:
            delete_order(order_id)
            messages.add_message(request, messages.INFO, "Удален заказ {}.".format(order_id))
        except Model.DoesNotExist :
            messages.add_message(request, messages.ERROR, "Не удалось удалить заказ {}.".format(order_id))
        return redirect("orders-list")