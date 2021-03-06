# Generated by Django 3.1 on 2021-06-27 08:14

import adv.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ADVLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(upload_to='adv', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpeg', 'jpg']), adv.models.CustomValidators.check_mime_type])),
                ('avtive', models.BooleanField(default=True)),
            ],
        ),
    ]
