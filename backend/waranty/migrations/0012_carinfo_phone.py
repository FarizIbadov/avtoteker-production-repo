# Generated by Django 3.1 on 2021-08-20 12:44

from django.db import migrations, models
import app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('waranty', '0011_remove_warrantytalon_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='carinfo',
            name='phone',
            field=models.CharField(max_length=255, null=True, validators=[app.validators.PhoneValidator], verbose_name='Telefon nomre'),
        ),
    ]