# Generated by Django 5.0.6 on 2024-06-28 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0005_cartdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='Ct_Product_Price',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
