# Generated by Django 3.1 on 2021-05-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_address_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='new',
            field=models.BooleanField(default=True),
        ),
    ]
