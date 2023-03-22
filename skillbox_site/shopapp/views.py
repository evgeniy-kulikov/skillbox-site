from django.http import HttpResponse, HttpRequest
from timeit import default_timer
from django.shortcuts import render


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
