# Generated by Django 3.1 on 2020-12-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specific', '0017_auto_20201223_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='free_service',
            field=models.BooleanField(default=False),
        ),
    ]
