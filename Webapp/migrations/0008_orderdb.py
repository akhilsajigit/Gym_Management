# Generated by Django 5.0.6 on 2024-06-29 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0007_alter_cartdb_ct_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Customer_State', models.CharField(blank=True, max_length=100, null=True)),
                ('Customer_Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Customer_City', models.CharField(blank=True, max_length=100, null=True)),
                ('Customer_Mobile', models.IntegerField(blank=True, null=True)),
                ('Customer_Email', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
