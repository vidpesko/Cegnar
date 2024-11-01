# Generated by Django 5.0.9 on 2024-11-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_socialsettings_personalsettings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personalsettings',
            options={'verbose_name': 'Nastavitve osebnih podatkov'},
        ),
        migrations.AddField(
            model_name='personalsettings',
            name='workshop_address',
            field=models.CharField(blank=True, max_length=20, verbose_name='Naslov delavnice'),
        ),
    ]