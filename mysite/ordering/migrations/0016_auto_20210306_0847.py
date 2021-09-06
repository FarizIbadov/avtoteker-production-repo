# Generated by Django 3.1 on 2021-03-06 08:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0075_remove_tire_image'),
        ('ordering', '0015_order_product_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='TireOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('product_title', models.CharField(blank=True, max_length=50)),
                ('product_link', models.CharField(blank=True, max_length=150)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('payment_type', models.PositiveSmallIntegerField(choices=[(1, 'Nağd'), (2, 'Kart ilə'), (3, 'Kreditlə'), (4, 'BirKart / TamKart ilə')], default=1)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('note', models.TextField(blank=True, null=True)),
                ('remember_me', models.BooleanField(default=False)),
                ('tire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tireapp.tire')),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
