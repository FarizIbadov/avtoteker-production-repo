# Generated by Django 3.1 on 2020-10-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("specific", "0005_auto_20200930_1417"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="description",
            field=models.TextField(default="description"),
        ),
        migrations.AlterField(
            model_name="brand",
            name="title",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="country",
            name="title",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="season",
            name="title",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="serie",
            name="description",
            field=models.TextField(default="description"),
        ),
        migrations.AlterField(
            model_name="serie",
            name="title",
            field=models.CharField(max_length=50),
        ),
    ]
