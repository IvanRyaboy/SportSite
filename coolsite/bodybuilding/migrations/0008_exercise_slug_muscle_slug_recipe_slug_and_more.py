# Generated by Django 4.2.5 on 2023-10-18 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodybuilding', '0007_sportnutrition_tierlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='muscle',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='sportnutrition',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='URL'),
        ),
    ]