# Generated by Django 3.1 on 2020-10-04 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tireapp", "0033_auto_20201004_1029"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tire",
            name="image",
            field=models.ImageField(
                default="default.png", null=True, upload_to="product"
            ),
        ),
    ]
