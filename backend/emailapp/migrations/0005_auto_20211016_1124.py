# Generated by Django 3.2.1 on 2021-10-16 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailapp', '0004_remove_email_is_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='email',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]