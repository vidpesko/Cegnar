# Generated by Django 5.0.9 on 2024-11-08 00:22

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_alter_factcard_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='intro_heading',
            field=wagtail.fields.RichTextField(blank=True, verbose_name='Naslov uvoda'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='intro_text',
            field=wagtail.fields.RichTextField(blank=True, help_text='Kratek uvod/opis sebe (da si strasten kovac)', verbose_name='Uvod'),
        ),
    ]
