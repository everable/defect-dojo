# Generated by Django 3.2.13 on 2022-06-22 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0163_system_settings_enable_calendar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='system_settings',
            name='staff_user_email_pattern',
        ),
    ]
