# Generated by Django 3.1.4 on 2022-06-17 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0011_profile_background_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='background_image',
        ),
    ]
