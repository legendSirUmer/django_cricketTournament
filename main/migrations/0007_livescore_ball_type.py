# Generated by Django 5.0.13 on 2025-05-03 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_livescorehistory_delete_nextmatch'),
    ]

    operations = [
        migrations.AddField(
            model_name='livescore',
            name='ball_type',
            field=models.CharField(choices=[('normal', 'Normal Ball'), ('white', 'White Ball'), ('no_ball', 'No Ball')], default='normal', max_length=10),
        ),
    ]
