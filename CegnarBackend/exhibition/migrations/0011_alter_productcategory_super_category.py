# Generated by Django 5.0.9 on 2024-11-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0010_productcategory_super_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='super_category',
            field=models.CharField(blank=True, help_text='Primer: nož, obesek,...', max_length=20, verbose_name='Ime nadkategorije'),
        ),
    ]
