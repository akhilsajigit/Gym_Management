# Generated by Django 5.0.6 on 2024-07-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0014_rename_membership_plans_membership_plansdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership_plansdb',
            name='Plan_Price',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
