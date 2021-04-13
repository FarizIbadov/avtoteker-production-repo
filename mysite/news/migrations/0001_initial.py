# Generated by Django 3.1 on 2021-04-13 08:46

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('title', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='campaign/')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('extra', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('order', models.PositiveSmallIntegerField(unique=True)),
                ('truncate', models.PositiveSmallIntegerField(default=150)),
            ],
        ),
    ]
