# Generated by Django 5.0.3 on 2024-04-17 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0006_alter_locationmodel_securitycode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationmodel',
            name='securityCode',
            field=models.CharField(editable=False, max_length=500, primary_key=True, serialize=False, unique=True),
        ),
    ]
