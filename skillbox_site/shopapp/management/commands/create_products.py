from django.core.management import BaseCommand
from shopapp.models import Product

"""
Создание management commands в Django  — команды, выполняемые из командной строки с помощью скрипта manage.py
Например для быстрого создания объектов модели при разработке.
Команды создаются в каталогах приложений (в подкаталоге app/management/commands). 
На каждую команду создается отдельный файл.
Из командной строки будут доступны файлы, кроме тех, которые начинаются со знака подчеркивания.
Команды создаются наследованием от класса django.core.management.base.BaseCommand. 
В простейшем случае достаточно переписать функцию handle.
Эта команда будет выполнена, а возвращаемый ею результат напечатается в консоли.

Данный файл выполняется следующей командой: 

python manage.py create_products

ссылки:
https://habr.com/ru/post/415049/
https://docs.djangoproject.com/en/2.0/howto/custom-management-commands/
"""


class Command(BaseCommand):  # имя класса должно быть "Command"
    """
    Создание новых продуктов в базе данных
    """
    def handle(self, *args, **options):  # имя функции должно быть "handle"
        # вывод информации перед созданием записи в БД
        self.stdout.write("Создание товара в БД")
        # self.stdout.write(self.style.SUCCESS("Создание продукта"))  # строка должна иметь цветовое выделение

        # список продуктов для записи
        products_names = [
            "Laptop",
            "Desktop",
            "Smartphone",
        ]
        for element in products_names:
            # получаем запись из БД или создаем если такой записи нет
            product, created = Product.objects.get_or_create(name=element)
            self.stdout.write(f"Создание продукта: {product.name}")  # строка созданного продукта

        # вывод информации при завершении записи в БД
        self.stdout.write(self.style.SUCCESS("Товары записаны в БД"))  # строка должна иметь цветовое выделение
