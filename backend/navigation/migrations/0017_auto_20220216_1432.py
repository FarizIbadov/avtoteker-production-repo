# Generated by Django 3.2.1 on 2022-02-16 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0016_urlname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navigationlink',
            name='link',
        ),
        migrations.AddField(
            model_name='navigationlink',
            name='url_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='navigation.urlname'),
        ),
    ]