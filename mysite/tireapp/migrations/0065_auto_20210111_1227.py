# Generated by Django 3.1 on 2021-01-11 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0064_auto_20210105_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tire',
            name='image',
            field=models.ImageField(default='', upload_to='product'),
        ),
    ]
