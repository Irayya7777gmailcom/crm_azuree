# Generated by Django 4.2 on 2023-11-21 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "Administrator",
            "0003_employeeactivities_alter_clientleads_assigned_to_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="empexcel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("age", models.CharField(max_length=30)),
                ("monthly_salary", models.CharField(max_length=30)),
            ],
        ),
    ]