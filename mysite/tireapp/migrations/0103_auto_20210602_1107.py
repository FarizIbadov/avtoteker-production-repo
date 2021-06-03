# Generated by Django 3.1 on 2021-06-02 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0102_auto_20210602_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tire',
            name='albalikart',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Yoxdur'), (3, '3 ay'), (6, '6 ay'), (12, '12 ay')]),
        ),
        migrations.AlterField(
            model_name='tire',
            name='birkart',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Yoxdur'), (2, '2 ay'), (3, '3 ay'), (6, '6 ay'), (9, '9 ay'), (12, '12 ay')]),
        ),
        migrations.AlterField(
            model_name='tire',
            name='bolkart',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Yoxdur'), (2, '2 ay'), (3, '3 ay'), (6, '6 ay'), (9, '9 ay'), (12, '12 ay')]),
        ),
        migrations.AlterField(
            model_name='tire',
            name='kredit',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Yoxdur'), (3, '3 ay'), (6, '6 ay'), (9, '9 ay'), (12, '12 ay')]),
        ),
        migrations.AlterField(
            model_name='tire',
            name='tamkart',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Yoxdur'), (2, '2 ay'), (3, '3 ay'), (6, '6 ay'), (9, '9 ay'), (12, '12 ay')]),
        ),
    ]
