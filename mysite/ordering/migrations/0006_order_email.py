# Generated by Django 3.1 on 2020-12-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0005_auto_20201204_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
