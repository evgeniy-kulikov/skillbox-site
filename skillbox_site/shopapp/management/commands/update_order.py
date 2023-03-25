from django.core.management import BaseCommand
from shopapp.models import Order, Product


# Заполняем таблицу связи ManyToMany между таблицами Order и Product: "shopapp_order_products"
# К существующему одному заказу привязываем все существующие товары
class Command(BaseCommand):  # имя класса должно быть "Command"
    def handle(self, *args, **options):  # имя функции должно быть "handle"
        self.stdout.write("Создание товара в БД")  # вывод информации перед созданием записи
        order = Order.objects.first()  # берем первый заказ (строку) из таблицы
        if not order:
            self.stdout.write("No order found")
            return  # если заказов нет, то прерываем
        # если заказ есть, то:
        products = Product.objects.all()

        # для того, что бы к заказу прикрепить продукты
        # используем менеджер связи ManyToMany - "order.products" где задействуем метод add()
        for product in products:
            order.products.add(product)

        order.save()

        self.stdout.write(
            self.style.SUCCESS(f"Products added successfully: {order.products.all()} to order: {order}")
        )

# Запуск файла на создание списка товаров в заказе:
# python manage.py update_order