# Generated by Django 3.1 on 2021-05-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0086_auto_20210522_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onestire',
            name='quantity',
            field=models.SmallIntegerField(default=0),
        ),
    ]
