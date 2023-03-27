# Generated by Django 4.1.7 on 2023-03-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopapp", "0006_order_products"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ["name", "price"], "verbose_name_plural": "products"},
        ),
        migrations.AlterField(
            model_name="order",
            name="products",
            field=models.ManyToManyField(
                related_name="orders_product", to="shopapp.product"
            ),
        ),
    ]
