# Generated by Django 3.1 on 2020-12-24 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0006_order_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]