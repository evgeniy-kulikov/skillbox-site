from django.contrib import admin
from shopapp.models import Product

# 1-й способ
# class ProductAdmin(admin.ModelAdmin):
#     list_display = "pk", "name", "description", "price", "discount", "arhived"
#     list_display_links = "pk", "name"
#
#
# admin.site.register(Product, ProductAdmin)


# 2-й способ (аналогичен первому)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display = "pk", "name", "description", "price", "discount", "arhived"
    list_display = "pk", "name", "description_short", "price", "discount", "arhived"   # меняем поле "description"
    list_display_links = "pk", "name"

    # Если функционал обрезания текста используется в приложении, то реализуем его в классе модели
    # Если этот функционал нужен только для админ-панели, то реализуем его файле shopapp/admin.py
    def description_short(self, obj: Product) -> str:
        """
        Обрезание текста поля "description" до 64 символов.
        :return: str
        """
        if len(obj.description) < 64:
            return obj.description
        return obj.description[:64] + "..."
