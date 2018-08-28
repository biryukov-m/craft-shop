# Generated by Django 2.0.6 on 2018-08-27 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20180827_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=30, null=True, verbose_name='URL в адресній стрічці броузера'),
        ),
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=30, null=True, verbose_name='URL в адресній стрічці броузера'),
        ),
        migrations.AddField(
            model_name='itemtype',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=30, null=True, verbose_name='URL в адресній стрічці броузера'),
        ),
        migrations.AddField(
            model_name='section',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=30, null=True, verbose_name='URL в адресній стрічці броузера'),
        ),
    ]