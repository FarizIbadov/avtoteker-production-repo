# Generated by Django 3.1 on 2021-05-22 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0088_auto_20210522_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onestire',
            name='year',
            field=models.PositiveSmallIntegerField(default=2021, null=True),
        ),
    ]
