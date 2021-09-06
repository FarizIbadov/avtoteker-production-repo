# Generated by Django 3.1 on 2021-06-27 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ADVPercentage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_percentage', models.FloatField()),
                ('second_percentage', models.FloatField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]