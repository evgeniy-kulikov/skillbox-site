import csv
from django.db.models import QuerySet
from django.db.models.options import Options
from django.http import HttpRequest, HttpResponse


"""
Класс для возможности записи в CSV файл данных из БД
"""
class ExportAsCSVMixin:
    def export_csv(self, request: HttpRequest, queryset: QuerySet):
        # метод для получения списка имен полей модели
        meta: Options = self.model._meta
        field_names = [item.name for item in meta.fields]

        # метод для записи результата (данных)
        response = HttpResponse(content_type="text/cvs")

        # Создание заголовка ответа для response
        # "attachment" организует скачивание файла
        response["Content-Disposition"] = f"attachment; filename={meta}-export.cvs"

        # запись результата в ответ
        csv_writer = csv.writer(response)

        # запись заголовков (в первой строчке будут имена полей)
        csv_writer.writerow(field_names)

        # будем записывать по одному объекту за раз
        for obj in queryset:
            csv_writer.writerow([getattr(obj, item) for item in field_names])

        return response

    # Указываем действию описание
    export_csv.short_description = "Export as CSV"
