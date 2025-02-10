# Generated by Django 5.1.6 on 2025-02-09 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0006_alter_department_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='status',
            field=models.CharField(blank=True, choices=[('ac', 'Active'), ('ic', 'Inactive'), ('pd', 'Pending')], default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
