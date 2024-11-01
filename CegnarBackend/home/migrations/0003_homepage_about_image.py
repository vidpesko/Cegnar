# Generated by Django 5.0.9 on 2024-10-29 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_homepage_about_btn_label_homepage_about_description_and_more'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='about_image',
            field=models.ForeignKey(blank=True, help_text='Slike mene', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
