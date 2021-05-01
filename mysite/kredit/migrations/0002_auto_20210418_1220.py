# Generated by Django 3.1 on 2021-04-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kredit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kredittype',
            name='link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='kredittype',
            name='link_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='kredittype',
            name='link_title',
            field=models.CharField(default='Click me', max_length=50),
            preserve_default=False,
        ),
    ]
