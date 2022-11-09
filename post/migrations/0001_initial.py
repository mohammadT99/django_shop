# Generated by Django 4.1.2 on 2022-10-19 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='image')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('crated', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('P', 'publish'), ('D', 'Draft')], max_length=1)),
            ],
        ),
    ]
