# Generated by Django 3.1 on 2021-09-20 06:26

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0016_auto_20210702_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description_az',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='description_tr',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='extra_2_az',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='extra_2_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='extra_2_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='extra_2_tr',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='extra_az',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='extra_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='extra_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='extra_tr',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image_az',
            field=models.ImageField(null=True, upload_to='campaign/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_en',
            field=models.ImageField(null=True, upload_to='campaign/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_ru',
            field=models.ImageField(null=True, upload_to='campaign/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_tr',
            field=models.ImageField(null=True, upload_to='campaign/'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_az',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_tr',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='truncate_az',
            field=models.PositiveSmallIntegerField(default=150, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='truncate_en',
            field=models.PositiveSmallIntegerField(default=150, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='truncate_ru',
            field=models.PositiveSmallIntegerField(default=150, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='truncate_tr',
            field=models.PositiveSmallIntegerField(default=150, null=True),
        ),
    ]