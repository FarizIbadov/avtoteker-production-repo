# Generated by Django 3.1 on 2020-12-04 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0004_auto_20201204_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
