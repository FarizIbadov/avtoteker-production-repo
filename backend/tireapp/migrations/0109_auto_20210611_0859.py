# Generated by Django 3.1 on 2021-06-11 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0108_tire_campains'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tire',
            old_name='campains',
            new_name='campaings',
        ),
    ]