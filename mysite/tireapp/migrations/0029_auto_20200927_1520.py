# Generated by Django 3.1 on 2020-09-27 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tireapp", "0028_auto_20200927_0832"),
    ]

    operations = [
        migrations.AlterField(
            model_name="extra",
            name="Class",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "Econom"), (2, "Orta"), (3, "Premium")]
            ),
        ),
    ]
