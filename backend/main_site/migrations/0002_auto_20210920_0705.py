# Generated by Django 3.1 on 2021-09-20 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tirelistmessage',
            name='text_az',
            field=models.CharField(default='Endirim', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tirelistmessage',
            name='text_en',
            field=models.CharField(default='Endirim', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tirelistmessage',
            name='text_ru',
            field=models.CharField(default='Endirim', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tirelistmessage',
            name='text_tr',
            field=models.CharField(default='Endirim', max_length=255, null=True),
        ),
    ]
