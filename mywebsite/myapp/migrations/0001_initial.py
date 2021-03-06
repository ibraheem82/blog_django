# Generated by Django 3.2.5 on 2022-04-21 04:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='imgs')),
                ('body', models.TextField()),
                ('post_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
