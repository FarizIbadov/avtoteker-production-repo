# Generated by Django 3.2.1 on 2022-02-08 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0043_auto_20220208_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='by_amount',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='by_percentage',
            field=models.BooleanField(default=False),
        ),
    ]