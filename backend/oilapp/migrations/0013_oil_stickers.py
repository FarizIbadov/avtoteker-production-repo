# Generated by Django 3.1 on 2021-06-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oilapp', '0012_auto_20210603_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='oil',
            name='stickers',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]