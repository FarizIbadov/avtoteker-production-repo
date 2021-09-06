# Generated by Django 3.1 on 2021-06-10 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0025_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='order_type',
            field=models.CharField(choices=[('t', 'Tire'), ('o', 'Oil')], max_length=1),
        ),
    ]