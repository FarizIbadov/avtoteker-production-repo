# Generated by Django 3.1 on 2021-09-20 07:05

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210512_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='description_az',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='description_tr',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='extra_az',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='extra_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='extra_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='extra_tr',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='image_az',
            field=models.ImageField(null=True, upload_to='news/'),
        ),
        migrations.AddField(
            model_name='news',
            name='image_en',
            field=models.ImageField(null=True, upload_to='news/'),
        ),
        migrations.AddField(
            model_name='news',
            name='image_ru',
            field=models.ImageField(null=True, upload_to='news/'),
        ),
        migrations.AddField(
            model_name='news',
            name='image_tr',
            field=models.ImageField(null=True, upload_to='news/'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_az',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_tr',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='truncate_az',
            field=models.PositiveSmallIntegerField(default=150, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='truncate_en',
            field=models.PositiveSmallIntegerField(default=150, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='truncate_ru',
            field=models.PositiveSmallIntegerField(default=150, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='truncate_tr',
            field=models.PositiveSmallIntegerField(default=150, null=True),
        ),
    ]