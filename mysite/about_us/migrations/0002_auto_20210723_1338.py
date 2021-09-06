# Generated by Django 3.1 on 2021-07-23 13:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maincontent',
            name='title',
        ),
        migrations.RemoveField(
            model_name='subcontent',
            name='title',
        ),
        migrations.AddField(
            model_name='maincontent',
            name='heading',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='subcontent',
            name='heading',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='maincontent',
            name='content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='subcontent',
            name='content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
