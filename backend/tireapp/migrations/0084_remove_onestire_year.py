# Generated by Django 3.1 on 2021-05-22 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0083_auto_20210522_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onestire',
            name='year',
        ),
    ]
