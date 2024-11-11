# Generated by Django 5.0.9 on 2024-11-10 21:24

import django.db.models.deletion
import modelcluster.fields
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0015_pageimage'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pageimage',
            name='page',
        ),
        migrations.RemoveField(
            model_name='pageimage',
            name='image',
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='To ni isto kot kategorija (pravilno: Lovski noz iz kaljenega jekla)', max_length=100, verbose_name='Ime noza')),
                ('image_description', wagtail.fields.RichTextField(blank=True, verbose_name='Kratek opis')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='exhibition.productcategory', verbose_name='Kategorija')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='exhibition.gallerypage')),
            ],
        ),
        migrations.DeleteModel(
            name='GalleryImages',
        ),
        migrations.DeleteModel(
            name='PageImage',
        ),
    ]
