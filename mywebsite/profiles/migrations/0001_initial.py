# Generated by Django 3.2.5 on 2022-05-17 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=200)),
                ('profession', models.CharField(max_length=200)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='assets/imgs')),
                ('about', models.TextField()),
                ('profile_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
