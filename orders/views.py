from django.contrib import messages, auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView

from general.services import get_total
from orders.models import Order
from orders.service import create_order, delete_order


class CreateOrder(LoginRequiredMixin,
                  # https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-loginrequiredmixin-mixin
                  View):  # https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#using-class-based-views
    # https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#view
    def post(self,
             request):  # https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#handling-forms-with-class-based-views
        user = request.user  # В запросе содержится пользователь. Проверить можно, остановившись на точке останова.
        password = request.POST.get("password")

        # https://docs.djangoproject.com/en/5.0/topics/auth/default/#authenticating-users
        password_correct = bool(auth.authenticate(request,
                                                  username=user.username,
                                                  password=password))

        if password_correct:
            new_order_id = create_order(user)

            # https://docs.djangoproject.com/en/5.0/ref/contrib/messages/
            messages.add_message(request, messages.INFO,
                                 "Ваш заказ номер {} принят к исполнению.".format(new_order_id))
            where_to_redirect = "orders-list"
        else:
            messages.add_message(request, messages.ERROR,
                                 "Неверный пароль")  # https://docs.djangoproject.com/en/5.0/ref/contrib/messages/
            where_to_redirect = "cart-detail"

        return redirect(where_to_redirect)  # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#redirect


class OrdersListView(LoginRequiredMixin,
                     # https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-loginrequiredmixin-mixin
                     ListView):  # https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#listview
    model = Order

    def get_queryset(
            self):  # https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_queryset
        result = Order.objects.filter(user=self.request.user).order_by(
            "-ordered_at")  # https://docs.djangoproject.com/en/5.0/ref/models/querysets/#filter
        # https://docs.djangoproject.com/en/5.0/ref/models/querysets/#order-by

        return result


class OrderDetailView(LoginRequiredMixin,
                      # https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-loginrequiredmixin-mixin
                      DetailView):  # https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#detailview
    model = Order

    def get_context_data(self, **kwargs):
        # Удобно посмотреть, как переопределить данный метод, в документации
        # к TemplateView.
        # https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#templateview
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.object.selectedproduct_set.all()
        context["grand_total"] = get_total(context["object_list"])
        return context


class DeleteOrder(LoginRequiredMixin,
                  # https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-loginrequiredmixin-mixin
                  View):  # https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#using-class-based-views
    # https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#view

    def post(self,
             request):  # # https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#handling-forms-with-class-based-views
        order_id = request.POST.get("order")

        try:
            delete_order(order_id)

            # https://docs.djangoproject.com/en/5.0/ref/contrib/messages/
            messages.add_message(request, messages.INFO, "Удален заказ {}.".format(order_id))
        except ObjectDoesNotExist:  # https://docs.djangoproject.com/en/5.0/ref/models/class/#doesnotexist

            # https://docs.djangoproject.com/en/5.0/ref/contrib/messages/
            messages.add_message(request, messages.ERROR, "Не удалось удалить заказ {}.".format(order_id))
        return redirect("orders-list")  # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#redirect
