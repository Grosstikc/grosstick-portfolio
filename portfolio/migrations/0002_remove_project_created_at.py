# Generated by Django 5.1.1 on 2024-09-24 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="created_at",
        ),
    ]
