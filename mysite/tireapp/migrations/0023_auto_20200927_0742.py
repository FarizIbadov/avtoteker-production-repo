# Generated by Django 3.1 on 2020-09-27 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("specific", "0003_auto_20200905_0924"),
        ("tireapp", "0022_auto_20200927_0742"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tire",
            name="manufacturer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="specific.country",
            ),
        ),
    ]
