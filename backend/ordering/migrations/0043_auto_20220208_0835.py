# Generated by Django 3.2.1 on 2022-02-08 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0042_auto_20220208_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='change_amount',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='change_percentage',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
