# Generated by Django 3.2.1 on 2022-02-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0044_auto_20220208_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='by_price_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='by_price_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='by_price_3',
            field=models.BooleanField(default=False),
        ),
    ]
