# Generated by Django 3.1 on 2021-08-20 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tireapp', '0115_size_size_code'),
        ('waranty', '0002_auto_20210820_0713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warrantytalon',
            name='tire',
        ),
        migrations.AddField(
            model_name='carinfo',
            name='warranty_talon',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_info', to='waranty.warrantytalon'),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='warranty_talon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pdf_set', to='waranty.warrantytalon'),
        ),
        migrations.CreateModel(
            name='CarTire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tireapp.tire')),
                ('warranty_talon', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='waranty.warrantytalon')),
            ],
        ),
    ]