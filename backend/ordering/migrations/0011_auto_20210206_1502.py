# Generated by Django 3.1 on 2021-02-06 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0075_remove_tire_image'),
        ('ordering', '0010_order_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tireapp.tire'),
        ),
    ]