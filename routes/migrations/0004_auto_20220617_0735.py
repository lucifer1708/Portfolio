# Generated by Django 3.1.4 on 2022-06-17 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0003_filters'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Filters',
        ),
        migrations.AddField(
            model_name='mywork',
            name='filter',
            field=models.CharField(choices=[('core', 'Core'), ('technology', 'Technology')], default='core', max_length=30),
        ),
        migrations.AlterField(
            model_name='experience',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='mywork',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='socialicon',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
