# Generated by Django 5.0.3 on 2024-04-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0008_alter_locationmodel_securitycode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationmodel',
            name='securityCode',
            field=models.CharField(editable=False, max_length=500, primary_key=True, serialize=False, unique=True),
        ),
    ]