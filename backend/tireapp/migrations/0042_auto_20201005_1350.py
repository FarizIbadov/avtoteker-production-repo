# Generated by Django 3.1 on 2020-10-05 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tireapp", "0041_tire_zr"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tire",
            name="description",
            field=models.TextField(default="description"),
        ),
    ]
