# Generated by Django 3.1 on 2021-06-11 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oilapp', '0013_oil_stickers'),
    ]

    operations = [
        migrations.AddField(
            model_name='oil',
            name='campaigns',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]