# Generated by Django 5.1.2 on 2024-11-02 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_rename_user_user_log'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_log',
            new_name='User',
        ),
    ]
