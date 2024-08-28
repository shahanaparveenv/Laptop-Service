# Generated by Django 5.0.7 on 2024-08-19 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptopservice_app', '0008_addtocart'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyNow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('buynow_status', models.BooleanField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_id', to='laptopservice_app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userid', to='laptopservice_app.customer')),
            ],
        ),
    ]
