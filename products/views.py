from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from products.models import Product


class ProductDetailView(DetailView):
    model = Product


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = Product.in_stock.all()
        return queryset
