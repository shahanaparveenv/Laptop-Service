# Generated by Django 5.0.7 on 2024-08-19 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptopservice_app', '0009_buynow'),
    ]

    operations = [
        migrations.AddField(
            model_name='buynow',
            name='totalprice',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
