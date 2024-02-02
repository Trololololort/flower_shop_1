"""
URL configuration for flower_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from accounts.views import SignUpView, IsLoginFreeView, ExtendedLoginView
from general.views import Instruction
from selected_products.views import AddToCart, CartDetailView
from companies.views import AboutCompanyView, ContactsView
from orders.views import CreateOrder, OrdersListView, OrderDetailView, DeleteOrder
from products.views import ProductDetailView, ProductListView, AreThereEnoughInStock

urlpatterns = [
      path("", ProductListView.as_view(), name="home"),
      path('admin/', admin.site.urls),

      path("accounts/login/", ExtendedLoginView.as_view(), name="login"),
      path("accounts/is-login-free/", IsLoginFreeView.as_view(), name="is-login-free"),
      path("accounts/signup/", SignUpView.as_view(), name="signup"),
      path("accounts/profile/", RedirectView.as_view(url=reverse_lazy('home'), permanent=False)),
      path("accounts/", include("django.contrib.auth.urls")),

      path('contacts/', ContactsView.as_view(), name="contacts"),

      path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
      path("products/", ProductListView.as_view(), name="product-list"),

      path("are-there-enough-in-stock/", AreThereEnoughInStock.as_view(), name="are-there-enough-in-stock"),

      path("about/", AboutCompanyView.as_view(), name="about"),

      path("cart/add/", AddToCart.as_view(), name="add-to-cart"),
      path("cart/", CartDetailView.as_view(), name="cart-detail"),

      path("orders/create/", CreateOrder.as_view(), name="create-order"),
      path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
      path("orders/delete/", DeleteOrder.as_view(), name="delete-order"),
      path("orders/", OrdersListView.as_view(), name="orders-list"),
      path("instruction/", Instruction.as_view(), name="instruction"),



  ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
