# Generated by Django 3.1 on 2020-12-25 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specific', '0019_brand_extra_one_year_quaranty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='extra_one_year_quaranty',
            new_name='extra_one_year_warranty',
        ),
    ]
