# Generated by Django 4.2 on 2023-08-30 08:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("demo_app", "0002_salestransaction_price_salestransaction_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.CharField(
                default="Medium", max_length=100, verbose_name="Product Category"
            ),
        ),
    ]
