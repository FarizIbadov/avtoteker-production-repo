# Generated by Django 3.1 on 2021-09-20 07:05

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oilapp', '0015_auto_20210611_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='description_az',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='description_tr',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='oil',
            name='des1_az',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='oil',
            name='des1_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='oil',
            name='des1_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='oil',
            name='des1_tr',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='oil',
            name='description_az',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='oil',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='oil',
            name='description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='oil',
            name='description_tr',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='serie',
            name='description_az',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='serie',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='serie',
            name='description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='serie',
            name='description_tr',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
