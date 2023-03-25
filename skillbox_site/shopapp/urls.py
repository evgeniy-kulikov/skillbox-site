from django.urls import path
from .apps import ShopappConfig
from .views import shop_index, groups_list, products_list, order_list

# Организация пространства имен для приложения
# app_name = "shopapp"  # можно так
app_name = ShopappConfig.name  # лучше так

urlpatterns = [
    path("", shop_index, name="index"),
    path("groups/", groups_list, name="groups_list"),
    path("products/", products_list, name="products_list"),
    path("orders/", order_list, name="orders_list"),
]
