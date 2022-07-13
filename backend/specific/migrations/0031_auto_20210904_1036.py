# Generated by Django 3.1 on 2021-09-04 10:36

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specific', '0030_auto_20210904_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='specific.brand'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='serie',
            name='extra',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='serie',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
