# Generated by Django 3.2.1 on 2022-02-03 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0004_pricecolors'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PriceColors',
            new_name='PriceColor',
        ),
    ]
