# Generated by Django 3.1 on 2021-06-03 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kredit_taksit', '0004_auto_20210603_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kredittaksitimage',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='kredittaksitinterval',
            name='deleted',
        ),
    ]
