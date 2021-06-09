# Generated by Django 3.1 on 2021-06-08 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oilapp', '0012_auto_20210603_0717'),
        ('tireapp', '0106_auto_20210604_1240'),
        ('ordering', '0021_auto_20210318_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oilorder',
            name='oil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='oilapp.oil'),
        ),
        migrations.AlterField(
            model_name='order',
            name='tire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tireapp.tire'),
        ),
    ]
