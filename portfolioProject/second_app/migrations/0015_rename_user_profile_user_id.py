# Generated by Django 3.2.9 on 2022-01-04 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0014_alter_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='user_id',
        ),
    ]
