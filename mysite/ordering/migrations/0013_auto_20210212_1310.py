# Generated by Django 3.1 on 2021-02-12 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0075_remove_tire_image'),
        ('ordering', '0012_remove_order_is_purchased'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tireapp.tire'),
        ),
    ]
