# Generated by Django 3.1 on 2020-10-11 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("specific", "0006_auto_20201003_1025"),
    ]

    operations = [
        migrations.AddField(
            model_name="brand",
            name="order_count",
            field=models.IntegerField(default=1),
        ),
    ]
