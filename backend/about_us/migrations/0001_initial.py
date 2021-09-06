# Generated by Django 3.1 on 2021-07-23 13:29

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField()),
                ('content', ckeditor.fields.RichTextField()),
                ('logo', models.ImageField(blank=True, upload_to='about_us/logo')),
                ('image', models.ImageField(blank=True, upload_to='about_us/image')),
                ('video', models.FileField(blank=True, upload_to='about_us/video', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField()),
                ('content', ckeditor.fields.RichTextField()),
                ('logo', models.ImageField(blank=True, upload_to='about_us/logo')),
                ('image', models.ImageField(blank=True, upload_to='about_us/image')),
                ('video', models.FileField(blank=True, upload_to='about_us/video', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('active', models.BooleanField(default=True)),
                ('main_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_contents', to='about_us.maincontent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]