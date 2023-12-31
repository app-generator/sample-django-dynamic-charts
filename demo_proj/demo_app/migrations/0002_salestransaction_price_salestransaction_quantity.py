# Generated by Django 4.2 on 2023-08-02 09:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("demo_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="salestransaction",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="salestransaction",
            name="quantity",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
    ]
