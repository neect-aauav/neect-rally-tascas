# Generated by Django 4.1.2 on 2022-10-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_teamsbars_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='qr_code',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
