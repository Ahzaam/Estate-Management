# Generated by Django 4.0.1 on 2022-06-10 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_alter_feedback_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='id',
            new_name='feebackid',
        ),
    ]
