from django.views.generic import DetailView, ListView

from products.forms import ProductSortFilterForm
from products.models import Product


class ProductDetailView(DetailView): # https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#detailview
    model = Product


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = Product.in_stock.all()

        category = self.request.GET.get("category")
        order_by = self.request.GET.get("order_by")

        if order_by:
            if order_by == 'price' or order_by == 'added':
                # По убыванию цены и даты добавления.
                queryset = queryset.order_by("-" + order_by)

            else:
                assert (order_by == 'category' or order_by == 'origin')
                queryset = queryset.order_by(order_by + "__name")

        if category:
            queryset = queryset.filter(category_id=category)

        return queryset

    def get_context_data(self, **kwargs):
        # Нам необходимо передать форму в контекст шаблона.
        #
        # Удобно взять пример на демонстрацию этого метода
        # в дкоументации TemplateView.
        # в https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#templateview
        # Метод get_context_data, располагается в миксине ContextMixin, от которого
        # наследуют и TemplateView, и ListView.

        context_data = super().get_context_data(**kwargs)

        # ProductSortFilterForm - это наследник ModelForm.
        # Поступивший в форму request.GET - это QuerySet, т.е. подобный словарю
        # объект. Мы передаем его в форму, чтобы наполнить ее данными.
        # Если параметров GET-запроса не было, то форма будет пустой.
        # Так мы не потеряем данные, которые ввел в форму пользователь.
        # https://docs.djangoproject.com/en/5.0/ref/forms/api/#bound-and-unbound-forms
        context_data["sort_filter_form"] = ProductSortFilterForm(self.request.GET)
        return context_data
