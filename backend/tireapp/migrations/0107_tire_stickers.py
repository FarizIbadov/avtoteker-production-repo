# Generated by Django 3.1 on 2021-06-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0106_auto_20210604_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='tire',
            name='stickers',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
