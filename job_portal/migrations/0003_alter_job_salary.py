# Generated by Django 5.1.2 on 2024-10-12 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0002_job_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
