# Generated by Django 3.1 on 2020-12-23 10:01

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specific', '0016_auto_20201223_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='description'),
        ),
    ]
