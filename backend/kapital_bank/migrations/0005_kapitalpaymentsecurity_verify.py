# Generated by Django 3.2.1 on 2022-02-05 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kapital_bank', '0004_auto_20220125_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='kapitalpaymentsecurity',
            name='verify',
            field=models.BooleanField(default=False),
        ),
    ]