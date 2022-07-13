# Generated by Django 3.1 on 2020-09-27 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tireapp", "0027_auto_20200927_0830"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tire",
            name="filters",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="tireapp.filter",
            ),
        ),
    ]
