# Generated by Django 5.1 on 2024-08-31 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envs', '0003_env_api_requests_env_createdat_env_updatedat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='env',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
