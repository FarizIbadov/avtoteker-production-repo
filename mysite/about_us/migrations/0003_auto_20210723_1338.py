# Generated by Django 3.1 on 2021-07-23 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0002_auto_20210723_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='maincontent',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subcontent',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]