# Generated by Django 3.1 on 2021-09-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0010_auto_20210920_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationlink',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]