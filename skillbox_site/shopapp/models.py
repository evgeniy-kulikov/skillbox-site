from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)  # decimal_places кол-во знаков после запятой
    discount = models.PositiveSmallIntegerField(default=0)  # скидка
    created_at = models.DateTimeField(auto_now_add=True)  # автоматическая запись текущего времени при создании
    arhived = models.BooleanField(default=False)



