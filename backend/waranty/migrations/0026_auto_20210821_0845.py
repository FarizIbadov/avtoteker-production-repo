# Generated by Django 3.1 on 2021-08-21 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waranty', '0025_auto_20210821_0814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='has_child',
            new_name='has_childs',
        ),
    ]