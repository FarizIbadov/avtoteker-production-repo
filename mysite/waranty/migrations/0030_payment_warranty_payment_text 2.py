# Generated by Django 3.1 on 2021-08-23 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waranty', '0029_auto_20210823_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='warranty_payment_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]