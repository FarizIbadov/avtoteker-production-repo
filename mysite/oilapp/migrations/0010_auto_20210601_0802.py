# Generated by Django 3.1 on 2021-06-01 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilapp', '0009_auto_20210601_0739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oil',
            name='taksit_12_month',
        ),
        migrations.RemoveField(
            model_name='oil',
            name='taksit_2_month',
        ),
        migrations.RemoveField(
            model_name='oil',
            name='taksit_3_month',
        ),
        migrations.RemoveField(
            model_name='oil',
            name='taksit_6_month',
        ),
        migrations.RemoveField(
            model_name='oil',
            name='taksit_9_month',
        ),
    ]
