# Generated by Django 3.2.1 on 2021-10-16 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kredit_taksit', '0006_kredittaksitinterval_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kredittaksitimage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='kredittaksitinterval',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
