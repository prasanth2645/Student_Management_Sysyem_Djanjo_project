# Generated by Django 5.1.3 on 2024-11-14 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organization", "0004_department_std"),
    ]

    operations = [
        migrations.CreateModel(
            name="Courses",
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
                ("name", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="Emp",
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
                ("title", models.CharField(max_length=25)),
                (
                    "course",
                    models.ManyToManyField(max_length=15, to="organization.courses"),
                ),
            ],
        ),
    ]