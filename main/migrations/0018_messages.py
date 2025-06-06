# Generated by Django 5.0.13 on 2025-05-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_livescorehistory_ball_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
