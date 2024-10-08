# Generated by Django 5.1 on 2024-08-30 10:13

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnvSecret',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('key', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Env',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=1000)),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', to_field='email')),
                ('key_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='envs.envsecret')),
            ],
            options={
                'unique_together': {('name', 'user')},
            },
        ),
    ]
