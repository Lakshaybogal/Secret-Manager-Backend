# Generated by Django 5.1 on 2024-08-31 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='env',
            name='access_password',
            field=models.CharField(default='', max_length=100),
        ),
    ]
