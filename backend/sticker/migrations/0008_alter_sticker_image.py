# Generated by Django 3.2.1 on 2021-10-30 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sticker', '0007_auto_20211016_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sticker',
            name='image',
            field=models.ImageField(blank=True, upload_to='sticker'),
        ),
    ]
