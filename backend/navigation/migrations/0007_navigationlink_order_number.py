# Generated by Django 3.1 on 2021-04-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0006_remove_navigationlink_show_in_navigation'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationlink',
            name='order_number',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]