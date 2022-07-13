# Generated by Django 3.1 on 2020-10-06 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tireapp", "0046_auto_20201006_1614"),
    ]

    operations = [
        migrations.CreateModel(
            name="Size",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("width", models.IntegerField(null=True)),
                ("height", models.CharField(max_length=10, null=True)),
                ("radius", models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="tire",
            name="height",
        ),
        migrations.RemoveField(
            model_name="tire",
            name="radius",
        ),
        migrations.RemoveField(
            model_name="tire",
            name="width",
        ),
        migrations.AddField(
            model_name="tire",
            name="size",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="tireapp.size",
            ),
        ),
    ]
