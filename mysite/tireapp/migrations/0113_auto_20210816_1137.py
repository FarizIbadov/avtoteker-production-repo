# Generated by Django 3.1 on 2021-08-16 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0112_auto_20210707_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tire',
            name='campaigns',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tire',
            name='stickers',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]