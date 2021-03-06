# Generated by Django 4.0.1 on 2022-06-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_tempuser_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoLoginToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='tempuser',
            name='otp',
            field=models.IntegerField(),
        ),
    ]
