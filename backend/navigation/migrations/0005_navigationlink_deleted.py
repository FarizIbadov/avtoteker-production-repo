# Generated by Django 3.1 on 2021-04-18 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0004_auto_20210418_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationlink',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]