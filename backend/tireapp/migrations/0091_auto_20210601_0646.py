# Generated by Django 3.1 on 2021-06-01 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0090_auto_20210522_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onestire',
            name='price_usd',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]