# Generated by Django 2.0.7 on 2018-09-21 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20180803_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=30, null=True, verbose_name='URL в адресній стрічці броузера'),
        ),
        migrations.AddField(
            model_name='color',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=30, null=True, verbose_name='URL в адресній стрічці броузера'),
        ),
        migrations.AddField(
            model_name='fabric',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=30, null=True, verbose_name='URL в адресній стрічці броузера'),
        ),
        migrations.AddField(
            model_name='gender',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=30, null=True, verbose_name='URL в адресній стрічці броузера'),
        ),
        migrations.AddField(
            model_name='size',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=30, null=True, verbose_name='URL в адресній стрічці броузера'),
        ),
    ]