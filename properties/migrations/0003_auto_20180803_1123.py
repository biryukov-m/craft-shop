# Generated by Django 2.0.6 on 2018-08-03 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20180710_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=models.TextField(max_length=30000, verbose_name='опис'),
        ),
        migrations.AlterField(
            model_name='fabric',
            name='description',
            field=models.TextField(max_length=30000, verbose_name='опис'),
        ),
    ]