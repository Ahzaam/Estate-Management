# Generated by Django 4.0.1 on 2022-06-07 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
    ]
