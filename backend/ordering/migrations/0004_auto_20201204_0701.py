# Generated by Django 3.1 on 2020-12-04 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0003_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=4),
        ),
    ]