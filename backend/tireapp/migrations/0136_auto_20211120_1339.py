# Generated by Django 3.2.1 on 2021-11-20 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0135_alter_tire_oe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tire',
            name='campaigns',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tire',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tire',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='tire',
            name='speed',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tire',
            name='stickers',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tire',
            name='tradeware',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tire',
            name='trim_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tire',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]