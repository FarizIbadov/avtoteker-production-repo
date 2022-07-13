# Generated by Django 3.2.1 on 2021-12-30 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0035_alter_order_taksit_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='taksit_choices',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, '---'), (2, '2 ay'), (3, '3 ay'), (6, '6 ay'), (9, '9 ay'), (12, '12 ay')], null=True),
        ),
    ]
