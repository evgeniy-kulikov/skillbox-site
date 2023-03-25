from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shopapp.models import Product, Order


class Command(BaseCommand):  # имя класса должно быть "Command"
    """
    Создание новых заказов в базе данных
    """
    def handle(self,  *args, **options):  # имя функции должно быть "handle"
        # вывод информации перед созданием записи в БД
        self.stdout.write("Создание заказа в БД")
        user = User.objects.get(username="admin")  # делаем заказ для существующего пользователя "admin"
        order = Order.objects.get_or_create(
            delivery_adress="Lenina street, bild. 1, apart 1",
            promocode="SALE123",
            user=user
        )
        self.stdout.write(f"Создан заказ {order}")

# Запуск файла на создание заказа:
# python manage.py create_order