# Generated by Django 3.2.1 on 2022-02-18 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0140_auto_20220209_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tire',
            name='tradeware',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]