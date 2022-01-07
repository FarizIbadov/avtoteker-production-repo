# Generated by Django 3.2.1 on 2022-01-07 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0137_alter_tire_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tire',
            old_name='kredit_initial_price',
            new_name='kredit_3_month_price',
        ),
        migrations.AddField(
            model_name='tire',
            name='kredit_6_month_price',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
