# Generated by Django 4.0.1 on 2022-06-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_alter_tempuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempuser',
            name='password',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=150),
        ),
    ]
