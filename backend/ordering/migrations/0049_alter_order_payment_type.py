# Generated by Django 3.2.1 on 2022-02-11 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0048_remove_order_by_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Nağd'), (2, 'Kart ilə'), (3, 'Kreditlə'), (4, 'BirKart'), (5, 'TamKart')], default=1),
        ),
    ]