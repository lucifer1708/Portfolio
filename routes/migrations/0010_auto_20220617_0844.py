# Generated by Django 3.1.4 on 2022-06-17 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0009_skills_text_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='image_icon',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='main_image_icons',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='text_number',
        ),
    ]
