# Generated by Django 3.1 on 2021-05-22 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0087_auto_20210522_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onestire',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
