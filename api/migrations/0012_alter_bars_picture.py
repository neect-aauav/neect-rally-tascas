# Generated by Django 4.1.2 on 2022-10-23 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_rename_visitd_bars_visited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bars',
            name='picture',
            field=models.TextField(default=None),
        ),
    ]
