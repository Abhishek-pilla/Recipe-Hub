# Generated by Django 5.0.7 on 2024-08-06 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_rename_recipe_recipes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='Recipe_Image',
        ),
    ]
