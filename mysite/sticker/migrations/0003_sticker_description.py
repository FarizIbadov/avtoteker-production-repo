# Generated by Django 3.1 on 2021-06-10 17:27

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sticker', '0002_auto_20210610_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='sticker',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]