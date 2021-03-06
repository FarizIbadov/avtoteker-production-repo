# Generated by Django 3.1 on 2020-09-13 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("specific", "0003_auto_20200905_0924"),
        ("tireapp", "0010_auto_20200913_0741"),
    ]

    operations = [
        migrations.CreateModel(
            name="Extra",
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
                ("montaj_balance", models.IntegerField(null=True)),
                ("razval", models.IntegerField(null=True)),
                ("year", models.PositiveSmallIntegerField(null=True)),
                (
                    "Class",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Premium"), (2, "Orta"), (3, "Econom")]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Filter",
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
                ("MS", models.BooleanField(default=False)),
                ("OE", models.BooleanField(default=False)),
                ("SL", models.BooleanField(default=False)),
                ("RF", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Kredit",
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
                ("value", models.PositiveSmallIntegerField(null=True)),
                ("month", models.PositiveSmallIntegerField(null=True)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="PriceDifference",
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
                ("value", models.PositiveSmallIntegerField(null=True)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Sale",
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
                ("value", models.PositiveSmallIntegerField(null=True)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="SelectFilter",
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
                ("tradeware", models.CharField(max_length=10, null=True)),
                ("weight", models.CharField(max_length=10, null=True)),
                ("speed", models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Taksit",
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
                ("value", models.PositiveSmallIntegerField(null=True)),
                ("month", models.PositiveSmallIntegerField(null=True)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name="tire",
            name="brand",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="specific.brand",
            ),
        ),
        migrations.AlterField(
            model_name="tire",
            name="manufacturer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="specific.country",
            ),
        ),
        migrations.AlterField(
            model_name="tire",
            name="season",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="specific.season",
            ),
        ),
        migrations.AlterField(
            model_name="tire",
            name="serie",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="specific.serie",
            ),
        ),
        migrations.AlterField(
            model_name="tire",
            name="size",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="tireapp.size",
            ),
        ),
        migrations.CreateModel(
            name="TaksitBox",
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
                ("active", models.BooleanField(default=True)),
                (
                    "nine_month",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nine_month",
                        to="tireapp.taksit",
                    ),
                ),
                (
                    "six_month",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="six_month",
                        to="tireapp.taksit",
                    ),
                ),
                (
                    "three_month",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="three_month",
                        to="tireapp.taksit",
                    ),
                ),
                (
                    "twelve_month",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="twelve_month",
                        to="tireapp.taksit",
                    ),
                ),
                (
                    "two_month",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="two_month",
                        to="tireapp.taksit",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Price",
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
                ("USDNO", models.PositiveSmallIntegerField(null=True)),
                (
                    "USD",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="tireapp.sale"
                    ),
                ),
                (
                    "USDOFF",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tireapp.pricedifference",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="KreditBox",
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
                ("active", models.BooleanField(default=True)),
                (
                    "nine_month",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nine_month",
                        to="tireapp.kredit",
                    ),
                ),
                (
                    "six_month",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="six_month",
                        to="tireapp.kredit",
                    ),
                ),
                (
                    "three_month",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="three_month",
                        to="tireapp.kredit",
                    ),
                ),
                (
                    "twelve_month",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="twelve_month",
                        to="tireapp.kredit",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="tire",
            name="extra",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="tireapp.extra",
            ),
        ),
        migrations.AddField(
            model_name="tire",
            name="filters",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="tireapp.filter",
            ),
        ),
        migrations.AddField(
            model_name="tire",
            name="kredit",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="tireapp.kreditbox",
            ),
        ),
        migrations.AddField(
            model_name="tire",
            name="price",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="tireapp.price",
            ),
        ),
        migrations.AddField(
            model_name="tire",
            name="select_filters",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="tireapp.selectfilter",
            ),
        ),
        migrations.AddField(
            model_name="tire",
            name="taksit",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="tireapp.taksitbox",
            ),
        ),
    ]
