# Generated by Django 5.0.9 on 2024-10-29 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='about_btn_label',
            field=models.CharField(blank=True, max_length=50, verbose_name='O meni - napis v gumbu'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='about_description',
            field=models.CharField(blank=True, max_length=50, verbose_name='O meni - kratek opis'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='about_title',
            field=models.CharField(blank=True, max_length=50, verbose_name='O meni - naslov'),
        ),
    ]
