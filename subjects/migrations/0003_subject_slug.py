# Generated by Django 5.1.6 on 2025-02-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_remove_subject_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
