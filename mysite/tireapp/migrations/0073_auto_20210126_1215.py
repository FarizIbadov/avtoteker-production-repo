# Generated by Django 3.1 on 2021-01-26 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0072_auto_20210126_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tire',
            name='kredit_12_dif',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='tire',
            name='kredit_3_dif',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='tire',
            name='kredit_6_dif',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='tire',
            name='kredit_9_dif',
            field=models.FloatField(default=0),
        ),
    ]