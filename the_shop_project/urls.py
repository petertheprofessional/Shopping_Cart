"""the_shop_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

import products.views
import clients.views
import shopping.views

urlpatterns = [
     path('categories/', products.views.categories),
     path('categories/<int:category_id>/', products.views.product_category_details),
     path('cart/<int:cart_id>/', shopping.views.cart),
     path('clients/<int:client_id>/', clients.views.client_details),
     path('clients/', clients.views.clients),
     path('products/<int:product_id>/', products.views.product_details),
     path('products/', products.views.products),
     path('admin/', admin.site.urls),
]
