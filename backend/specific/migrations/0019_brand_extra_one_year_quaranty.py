# Generated by Django 3.1 on 2020-12-25 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specific', '0018_brand_free_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='extra_one_year_quaranty',
            field=models.BooleanField(default=False),
        ),
    ]