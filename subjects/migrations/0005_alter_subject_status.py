# Generated by Django 5.1.6 on 2025-02-09 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0004_alter_subject_status_delete_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='status',
            field=models.CharField(blank=True, choices=[('ac', 'Active'), ('in', 'Inactive')], max_length=100),
        ),
    ]
