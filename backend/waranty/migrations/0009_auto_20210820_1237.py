# Generated by Django 3.1 on 2021-08-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waranty', '0008_warrantytalon_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warrantytalon',
            name='title',
            field=models.CharField(default='Avtoteker Talon', max_length=100, null=True),
        ),
    ]