# Generated by Django 4.1.1 on 2023-04-17 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0015_rename_booked_user_booking_first_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='first_name',
            new_name='user',
        ),
    ]