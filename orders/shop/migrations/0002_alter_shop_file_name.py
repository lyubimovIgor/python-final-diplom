# Generated by Django 4.1.6 on 2023-10-25 15:56

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shop",
            name="file_name",
            field=models.FileField(
                blank=True,
                null=True,
                storage=django.core.files.storage.FileSystemStorage(
                    location="/home/igor/Рабочий стол/python-final-diplom/orders/storage"
                ),
                upload_to="",
                verbose_name="",
            ),
        ),
    ]