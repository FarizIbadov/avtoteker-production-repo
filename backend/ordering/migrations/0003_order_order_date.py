# Generated by Django 3.1 on 2020-12-03 18:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0002_auto_20201203_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]