# Generated by Django 3.1 on 2021-09-06 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0121_auto_20210905_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='TireClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tire',
            name='Class',
        ),
    ]