# Generated by Django 5.1.7 on 2025-03-25 10:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portpolio", "0007_alter_internship_phonenumber"),
    ]

    operations = [
        migrations.AlterField(
            model_name="internship",
            name="usn",
            field=models.BooleanField(max_length=60),
        ),
    ]
