# Generated by Django 3.2.1 on 2022-07-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_news_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='viewed_by',
            field=models.PositiveSmallIntegerField(default=0, editable=False, null=True),
        ),
    ]
