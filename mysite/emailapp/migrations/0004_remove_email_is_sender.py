# Generated by Django 3.1 on 2021-06-19 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailapp', '0003_authuser_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='is_sender',
        ),
    ]
