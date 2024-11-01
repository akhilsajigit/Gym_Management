# Generated by Django 5.0.6 on 2024-06-28 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0004_rename_trainer_register_trainer_registerdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ct_User', models.CharField(blank=True, max_length=100, null=True)),
                ('Ct_Product_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Ct_Quantity', models.IntegerField(blank=True, null=True)),
                ('Ct_Total_price', models.IntegerField(blank=True, null=True)),
                ('Ct_Image', models.ImageField(blank=True, null=True, upload_to='Cart Images')),
            ],
        ),
    ]
