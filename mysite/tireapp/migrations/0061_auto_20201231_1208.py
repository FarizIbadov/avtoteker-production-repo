# Generated by Django 3.1 on 2020-12-31 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0060_auto_20201231_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tire',
            name='image',
            field=models.ImageField(default='default/default.png', upload_to='product'),
        ),
    ]
