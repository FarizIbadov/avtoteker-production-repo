# Generated by Django 3.1 on 2020-09-25 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tireapp", "0018_auto_20200924_1405"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="size",
            name="ZR_R",
        ),
        migrations.AddField(
            model_name="filter",
            name="ZR_R",
            field=models.BooleanField(default=False),
        ),
    ]
