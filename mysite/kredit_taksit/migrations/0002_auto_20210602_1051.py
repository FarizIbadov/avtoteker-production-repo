# Generated by Django 3.1 on 2021-06-02 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kredit_taksit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kredittaksitimage',
            name='name',
            field=models.CharField(choices=[('birkart', 'Birkart'), ('tamkart', 'Tamkart'), ('bolkart', 'Bolkart'), ('albalikart', 'Albalikart'), ('kredit', 'Kredit')], max_length=20),
        ),
    ]