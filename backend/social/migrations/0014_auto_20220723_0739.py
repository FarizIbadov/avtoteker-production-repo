# Generated by Django 3.2.1 on 2022-07-23 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0013_auto_20220722_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='latidude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
