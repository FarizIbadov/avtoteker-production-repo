# Generated by Django 3.1 on 2021-06-04 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0104_auto_20210603_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tire',
            name='code',
            field=models.CharField(blank=True, default='XXX', max_length=200),
        ),
    ]
