# Generated by Django 3.1 on 2021-01-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0073_auto_20210126_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='tire',
            name='new',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tire',
            name='outlet',
            field=models.BooleanField(default=False),
        ),
    ]
