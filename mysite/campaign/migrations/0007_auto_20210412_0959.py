# Generated by Django 3.1 on 2021-04-12 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0006_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=150),
        ),
    ]