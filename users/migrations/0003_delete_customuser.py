# Generated by Django 5.1.6 on 2025-02-12 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_delete_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
