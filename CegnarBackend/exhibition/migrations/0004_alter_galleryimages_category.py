# Generated by Django 5.0.9 on 2024-11-08 01:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0003_galleryimages_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimages',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exhibition.productcategory'),
        ),
    ]
