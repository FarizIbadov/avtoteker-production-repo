# Generated by Django 3.1 on 2021-03-06 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oilapp', '0005_auto_20210227_1204'),
        ('ordering', '0018_oilorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oilorder',
            name='oil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='oilapp.oil'),
        ),
    ]
