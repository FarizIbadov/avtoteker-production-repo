# Generated by Django 3.1 on 2020-09-13 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tireapp", "0009_auto_20200913_0719"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tire",
            name="quantity",
            field=models.PositiveIntegerField(null=True),
        ),
    ]
