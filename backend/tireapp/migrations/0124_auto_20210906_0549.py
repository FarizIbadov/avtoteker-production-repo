# Generated by Django 3.1 on 2021-09-06 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0123_tire_class'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tire',
            old_name='Class',
            new_name='tire_class',
        ),
    ]