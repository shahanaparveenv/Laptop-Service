# Generated by Django 5.0.7 on 2024-08-23 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptopservice_app', '0011_buynow_address_buynow_phone_buynow_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buynow',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='buynow',
            name='post',
            field=models.CharField(max_length=6),
        ),
    ]
