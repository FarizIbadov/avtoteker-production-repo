# Generated by Django 3.1 on 2020-10-04 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tireapp", "0040_remove_tire_zr_r"),
    ]

    operations = [
        migrations.AddField(
            model_name="tire",
            name="ZR",
            field=models.BooleanField(default=False),
        ),
    ]
