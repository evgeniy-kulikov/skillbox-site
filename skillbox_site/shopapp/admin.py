from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from shopapp.models import Product, Order
from shopapp.admin_mixins import ExportAsCSVMixin

""" Простое отображение полей таблиц в админке """
#  #  # 1-й способ
#  # class ProductAdmin(admin.ModelAdmin):
#  #     list_display = "pk", "name", "description", "price", "discount", "archived"
#  #     list_display_links = "pk", "name"
#  #
#  # admin.site.register(Product, ProductAdmin)

#  #  # 2-й способ (аналогичен первому)
#  # @admin.register(Product)
#  # class ProductAdmin(admin.ModelAdmin):
#  #     list_display = "pk", "name", "description", "price", "discount", "archived"
#  #     list_display_links = "pk", "name"
#  #     ordering = "pk",  # "-pk" сортировка в обратном порядке
#  #     search_fields = "name", "description"  # поиск по содержимому полей


#  # @admin.register(Order)
#  # class OrderAdmin(admin.ModelAdmin):
#  #     list_display = "delivery_adress", "promocode", "created_at", "user"
#  #
#  #     # в админке на странице заказов разные пользователи будут загружаться не отдельными запросами, а сразу одним.
#  #     def get_queryset(self, request):
#  #         # return Order.objects.select_related("user")
#  #         return Order.objects.select_related("user").prefetch_related("products")
#  #


""" Вариант с привязкой связанных полей из другой таблицы (через внешний ключ) + разные варианты отображения полей """


class OrderInLane(admin.TabularInline):
    """Отобразим на странице продуктов связанные заказы (для конкретного продукта)"""
    model = Product.orders_product.through  # related_name="orders_product" (в таблице "Order")


# Чтобы функция стала действием, ее надо декорировать @admin.action(description="<Описание действия>")
@admin.action(description="Archive products (архивация продукта)")
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    """
    Создание группового действия по архивированию продукта в разделе "Products"
    :param modeladmin:
    :param request:
    :param queryset:
    :return:
    """
    queryset.update(archived=True)
    # Дальше эту функцию нужно связать с нужным разделом админки, через указания свойства:  actions = [<имя функции>,]


@admin.action(description="Unarchive products (разархивация продукта)")
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    """
    Создание группового действия по разархивированию продукта в разделе "Products"
    :param modeladmin:
    :param request:
    :param queryset:
    :return:
    """
    queryset.update(archived=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        "export_csv",  # действие для записи файла на экспорт данных
    ]
    inlines = [
        OrderInLane,
    ]
    # list_display = "pk", "name", "description", "price", "discount", "archived"
    list_display = "pk", "name", "description_short", "price", "discount", "archived"   # меняем поле "description"
    list_display_links = "pk", "name"
    ordering = "pk",  # "-pk" сортировка в обратном порядке
    search_fields = "name", "description"  # поиск по содержимому полей

    # Дополнительное управление секциями полей (Группировка полей)
    fieldsets = [
        (None, {
           "fields": ("name", "description"),
        }),
        ("Price options", {
            "fields": ("price", "discount"),
            "classes": ("wide", "collapse",),
        }),
        ("Extra options", {
            "fields": ("archived",),
            "classes": ("collapse",),
            "description": "Дополнение. Поле 'archived' архивация при удалении"
        })
    ]

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


# TabularInline и StackedInline дают одинаковый результат, но отображаются немного по другому
# class ProductInLine(admin.TabularInline):
class ProductInLine(admin.StackedInline):
    """Отобразим на странице заказов связанные продукты (для конкретного заказа)"""
    model = Order.products.through  # свойство "through" позволяет взять продукты через заказ


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInLine,
    ]
    list_display = "delivery_adress", "promocode", "created_at", "user_verbose"

    # в админке на странице заказов разные пользователи будут загружаться не отдельными запросами, а сразу одним.
    def get_queryset(self, request):
        # return Order.objects.select_related("user")
        return Order.objects.select_related("user").prefetch_related("products")

    # Выводим в админке на странице заказов имя пользователя (при отсутствии его будет выведен логин)
    def user_verbose(selfs, obj: Order) -> str:
        return obj.user.first_name or obj.user.username
