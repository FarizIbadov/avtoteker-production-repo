# Generated by Django 3.2.1 on 2022-06-07 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0148_alter_tire_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tire',
            options={'ordering': ('-brand__order_number', 'order_number')},
        ),
    ]