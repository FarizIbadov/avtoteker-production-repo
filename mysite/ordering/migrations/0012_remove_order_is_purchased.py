# Generated by Django 3.1 on 2021-02-10 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0011_auto_20210206_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_purchased',
        ),
    ]
