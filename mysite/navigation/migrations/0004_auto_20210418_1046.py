# Generated by Django 3.1 on 2021-04-18 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0003_auto_20210418_1027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='navigationlink',
            old_name='active',
            new_name='show_in_navigation',
        ),
    ]
