# Generated by Django 3.1 on 2021-01-19 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='add')),
                ('duration', models.PositiveSmallIntegerField(default=1000)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
