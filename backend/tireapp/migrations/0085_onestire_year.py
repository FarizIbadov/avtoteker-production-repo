# Generated by Django 3.1 on 2021-05-22 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0084_remove_onestire_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='onestire',
            name='year',
            field=models.PositiveSmallIntegerField(default=2021),
        ),
    ]