# Generated by Django 5.0.9 on 2024-11-10 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0021_galleryactualimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryactualimage',
            name='name',
        ),
    ]
