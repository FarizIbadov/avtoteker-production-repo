# Generated by Django 3.2.1 on 2022-07-21 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0011_auto_20211016_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='label',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.CharField(max_length=255, null=True),
        ),
    ]