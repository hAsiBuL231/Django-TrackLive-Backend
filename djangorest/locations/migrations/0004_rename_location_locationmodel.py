# Generated by Django 5.0.3 on 2024-04-04 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_rename_locationmodel_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Location',
            new_name='LocationModel',
        ),
    ]