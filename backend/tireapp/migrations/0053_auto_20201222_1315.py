# Generated by Django 3.1 on 2020-12-22 13:15

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0052_auto_20201221_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tire',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='description'),
        ),
    ]