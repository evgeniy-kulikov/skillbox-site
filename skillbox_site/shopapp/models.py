from django.contrib.auth.models import User
from django.db import models

"""
Опции полей:
null
По умолчанию установлено значение False (т.е. должно быть значение)
Избегайте использования null в строковых полях, таких как CharField и TextField. 
Если строковое поле имеет значение null=True, это означает, 
что у него есть два возможных значения для «нет данных»: NULL и пустая строка. 
соглашение Django заключается в использовании пустой строки, а не NULL
Единственное исключение - когда a CharField имеет оба значения: unique=True и blank=True. 
В этой ситуации требуется null=True, 
чтобы избежать нарушений ограничений при сохранении нескольких объектов с пустыми значениями.


blank
По умолчанию установлено значение False (т.е. должно быть значение)
Если поле имеет blank=True, проверка формы позволит ввести пустое значение. 
Если поле имеет blank=False, поле будет обязательным.
"""


# Create your models here.
class Product(models.Model):

    class Meta:
        ordering = ["name", "price"]  # Сортировка по полю. В обратном прядке ["-name"]
        verbose_name_plural = "products"  # Множественное имя
        # db_table = "electronic_product"  # Отображение имени таблицы в БД (не не для модулей приложения django)

    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)  # null=False - можно не писать. Это значение по умолчанию
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)  # decimal_places кол-во знаков после запятой
    discount = models.PositiveSmallIntegerField(default=0)  # скидка
    created_at = models.DateTimeField(auto_now_add=True)  # автоматическая запись текущего времени при создании
    arhived = models.BooleanField(default=False)


class Order(models.Model):
    delivery_adress = models.TextField(null=True, blank=True)  # null=True - плохое решение
    promocode = models.CharField(max_length=20, null=False, blank=True)  # null=False - можно не писать. Это значение по умолчанию
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name="orders")
