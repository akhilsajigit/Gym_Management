# Generated by Django 5.0.6 on 2024-07-07 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0007_rename_category_image_workout_categorydb_workout_cat_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Workout_CategoryDB',
            new_name='SingWrk_Cat_DB',
        ),
    ]
