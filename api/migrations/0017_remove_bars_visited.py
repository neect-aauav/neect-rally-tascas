# Generated by Django 4.1.2 on 2022-10-26 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_remove_games_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bars',
            name='visited',
        ),
    ]
