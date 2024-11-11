# Generated by Django 5.0.9 on 2024-11-10 21:40

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0018_galleryimage_created_at'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryimage',
            name='image',
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Ustvarjeno'),
        ),
        migrations.CreateModel(
            name='GalleryActualImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
                ('snippet', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='exhibition.galleryimage')),
            ],
        ),
    ]