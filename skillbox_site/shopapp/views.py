from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest
from timeit import default_timer
from django.shortcuts import render
from shopapp.models import Product


# def shop_index(request: HttpRequest):  # нотация для request
#     # Вывод информации в терминал
#     print(request.path)
#     print(request.method)
#     print(request.headers)
#     return HttpResponse("<h1>Страница shop</h1>")

def shop_index(request):
    products = [
        ("Printer", 1800),
        ("Destop", 3050),
        ("Mouse", 50),
    ]
    context = {
        "time_running": default_timer(),
        "products": products,
    }
    return render(request, "shopapp/shop-index.html", context=context)


def groups_list(request: HttpRequest):
    context = {
        # "groups": Group.objects.all(),
        # prefetch_related выполняет отдельный поиск для каждой связи, уменьшая кол-во запросов к БД
        "groups": Group.objects.prefetch_related("permissions").all(),
    }
    return render(request, "shopapp/group-list.html", context=context)

def products_list(request: HttpRequest):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, "shopapp/products-list.html", context=context)
