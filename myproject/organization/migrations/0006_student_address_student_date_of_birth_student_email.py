# Generated by Django 5.1.3 on 2024-11-18 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organization", "0005_courses_emp"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="student",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="student",
            name="email",
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
