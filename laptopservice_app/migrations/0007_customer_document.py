# Generated by Django 5.0.7 on 2024-08-16 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptopservice_app', '0006_product_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='document',
            field=models.FileField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]
