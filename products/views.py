from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from products.forms import ProductSortFilterForm
from products.models import Product


class ProductDetailView(DetailView):
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
        context_data = super().get_context_data(**kwargs)
        context_data["sort_filter_form"] = ProductSortFilterForm(self.request.GET)
        return context_data
