# Generated by Django 3.1 on 2020-10-04 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tireapp", "0039_auto_20201004_1158"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tire",
            name="ZR_R",
        ),
    ]
