# Generated by Django 4.1.2 on 2022-10-23 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='nmec',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
