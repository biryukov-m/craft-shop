# Generated by Django 2.0.6 on 2019-01-02 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_auto_20180921_0622'),
        ('product', '0018_auto_20190102_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='size_height',
        ),
        migrations.RemoveField(
            model_name='item',
            name='size_width',
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.ManyToManyField(to='properties.Size', verbose_name='розміри'),
        ),
    ]