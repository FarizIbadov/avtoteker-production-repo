# Generated by Django 3.1 on 2020-10-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tireapp", "0042_auto_20201005_1350"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tire",
            name="quantity",
            field=models.PositiveIntegerField(default=4),
        ),
    ]
